import asyncio
import os
import secrets
import socket
import ssl
import sys
from datetime import datetime

_core = sys.modules.get("main") or sys.modules.get("__main__")
if _core is None:
    raise RuntimeError("core module not found")
LINKS = _core.LINKS
LINKS_LOCK = _core.LINKS_LOCK
stats = _core.stats
hourly_traffic = _core.hourly_traffic
connections = _core.connections
error_logs = _core.error_logs
logger = _core.logger
is_link_allowed = _core.is_link_allowed
is_ip_allowed = _core.is_ip_allowed
save_state = _core.save_state
log_activity = _core.log_activity
now_ir = _core.now_ir
TCP_PORT = _core.TCP_PORT
TCP_TLS_ENABLED = _core.TCP_TLS_ENABLED
from relay_vless import check_and_use
from speed_limit import throttle

TCP_BUF = 4 * 1024 * 1024
BATCH_THRESHOLD = 100
FLOW_HIGH_WATER = 8 * 1024 * 1024
CONNECT_TIMEOUT = 10.0
HEADER_TIMEOUT = 15.0


def _tune_socket(writer: asyncio.StreamWriter):
    sock = writer.transport.get_extra_info("socket")
    if not sock:
        return
    try:
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 64 * 1024 * 1024)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 64 * 1024 * 1024)
    except OSError:
        pass
    try:
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_CORK, 0)
    except (OSError, AttributeError):
        pass


def _uuid_from_bytes(raw: bytes) -> str:
    h = raw.hex()
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:32]}"


async def _read_vless_header(reader: asyncio.StreamReader):
    await reader.readexactly(1)
    uuid_raw = await reader.readexactly(16)
    addon_len = (await reader.readexactly(1))[0]
    if addon_len:
        await reader.readexactly(addon_len)
    command = (await reader.readexactly(1))[0]
    port = int.from_bytes(await reader.readexactly(2), "big")
    addr_type = (await reader.readexactly(1))[0]
    if addr_type == 1:
        address = ".".join(str(b) for b in await reader.readexactly(4))
    elif addr_type == 2:
        dlen = (await reader.readexactly(1))[0]
        address = (await reader.readexactly(dlen)).decode("utf-8", errors="ignore")
    elif addr_type == 3:
        ab = await reader.readexactly(16)
        address = ":".join(f"{ab[i]:02x}{ab[i+1]:02x}" for i in range(0, 16, 2))
    else:
        raise ValueError(f"unknown addr type: {addr_type}")
    return _uuid_from_bytes(uuid_raw), command, address, port


async def _relay_client_to_remote(reader: asyncio.StreamReader, writer: asyncio.StreamWriter, conn_id: str, uid: str):
    pending_bytes = 0
    pending_reqs = 0
    try:
        while True:
            data = await reader.read(TCP_BUF)
            if not data:
                break
            nd = len(data)
            pending_bytes += nd
            pending_reqs += 1
            if pending_reqs >= BATCH_THRESHOLD:
                hourly_traffic[now_ir().strftime("%H:00")] += pending_bytes
                if not await check_and_use(uid, pending_bytes):
                    break
                await throttle(uid, pending_bytes)
                stats["total_requests"] += pending_reqs
                connections[conn_id]["bytes"] += pending_bytes
                pending_bytes = 0
                pending_reqs = 0
            writer.write(data)
            if writer.transport.get_write_buffer_size() > FLOW_HIGH_WATER:
                await writer.drain()
        if pending_bytes > 0:
            hourly_traffic[now_ir().strftime("%H:00")] += pending_bytes
            if await check_and_use(uid, pending_bytes):
                await throttle(uid, pending_bytes)
                stats["total_requests"] += pending_reqs
                connections[conn_id]["bytes"] += pending_bytes
    except (asyncio.CancelledError, Exception):
        pass


async def _relay_remote_to_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter, conn_id: str, uid: str):
    pending_bytes = 0
    pending_reqs = 0
    try:
        while True:
            data = await reader.read(TCP_BUF)
            if not data:
                break
            nd = len(data)
            pending_bytes += nd
            pending_reqs += 1
            if pending_reqs >= BATCH_THRESHOLD:
                hourly_traffic[now_ir().strftime("%H:00")] += pending_bytes
                if not await check_and_use(uid, pending_bytes):
                    break
                await throttle(uid, pending_bytes)
                stats["total_requests"] += pending_reqs
                connections[conn_id]["bytes"] += pending_bytes
                pending_bytes = 0
                pending_reqs = 0
            writer.write(data)
            if writer.transport.get_write_buffer_size() > FLOW_HIGH_WATER:
                await writer.drain()
        if pending_bytes > 0:
            hourly_traffic[now_ir().strftime("%H:00")] += pending_bytes
            if await check_and_use(uid, pending_bytes):
                await throttle(uid, pending_bytes)
                stats["total_requests"] += pending_reqs
                connections[conn_id]["bytes"] += pending_bytes
    except (asyncio.CancelledError, Exception):
        pass


async def _handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    peer = writer.get_extra_info("peername")
    ip = peer[0] if peer else "unknown"
    conn_id = None
    remote_writer = None
    try:
        uuid, command, address, port = await asyncio.wait_for(
            _read_vless_header(reader), timeout=HEADER_TIMEOUT
        )
        if command != 1:
            return

        async with LINKS_LOCK:
            link = LINKS.get(uuid)
        if not is_link_allowed(link):
            return
        if not is_ip_allowed(link, uuid, ip):
            log_activity("connection", f"Rejected {ip} (IP limit)", "warn")
            return

        conn_id = secrets.token_urlsafe(6)
        connections[conn_id] = {
            "uuid": uuid,
            "ip": ip,
            "transport": "vless-tcp",
            "connected_at": datetime.now().isoformat(),
            "bytes": 0,
        }

        remote_reader, remote_writer = await asyncio.wait_for(
            asyncio.open_connection(address, port), timeout=CONNECT_TIMEOUT
        )
        _tune_socket(remote_writer)

        done, pending = await asyncio.wait(
            {
                asyncio.create_task(_relay_client_to_remote(reader, remote_writer, conn_id, uuid)),
                asyncio.create_task(_relay_remote_to_client(remote_reader, writer, conn_id, uuid)),
            },
            return_when=asyncio.FIRST_COMPLETED,
        )
        for t in pending:
            t.cancel()
            try:
                await t
            except asyncio.CancelledError:
                pass

        asyncio.create_task(save_state())
    except asyncio.TimeoutError:
        stats["total_errors"] += 1
    except Exception as exc:
        stats["total_errors"] += 1
        error_logs.append({"error": str(exc), "time": datetime.now().isoformat()})
    finally:
        if remote_writer:
            try:
                remote_writer.close()
                await remote_writer.wait_closed()
            except Exception:
                pass
        try:
            writer.close()
        except Exception:
            pass
        if conn_id:
            connections.pop(conn_id, None)


async def start_tcp_server():
    ssl_ctx = None
    if TCP_TLS_ENABLED:
        try:
            ssl_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            ssl_ctx.load_cert_chain(os.environ["TLS_CERT"], os.environ["TLS_KEY"])
        except Exception as exc:
            logger.warning(f"TLS load failed ({exc}) — running TCP listener without TLS")
            ssl_ctx = None
    try:
        server = await asyncio.start_server(
            _handle_client, "0.0.0.0", TCP_PORT, ssl=ssl_ctx
        )
        logger.info(f"TCP VLESS listener active on port {TCP_PORT} (TLS={'on' if ssl_ctx else 'off'})")
        log_activity("system", f"TCP VLESS listener active on port {TCP_PORT}", "ok")
        async with server:
            await server.serve_forever()
    except Exception as exc:
        logger.warning(f"TCP VLESS listener failed to start on {TCP_PORT}: {exc}")
