# Cyber-Rage Panel Speed

High-performance VLESS tunneling panel built with FastAPI — optimized for Iranian networks and beyond.

## Features

- **3 tunnel protocols** per config:
  - `VLESS + WebSocket` — classic, works through CDNs (Cloudflare)
  - `VLESS + TCP` — raw TCP relay, fastest throughput (own TCP listener, optional TLS)
  - `XHTTP (packet-up / stream-up)` — sizing-v10 XHTTP, most DPI-resistant
- **Clean IP Repository** — paste clean IPs into a config; the generated link connects to the clean IP while keeping your domain as SNI/Host (Cloudflare-bypass pattern). The original domain-based link is shown as a secondary row for fallback.
- **Fragment support** — `fragment=tcp,100,150` parameter to bypass DPI packet inspection
- Fingerprint (chrome/firefox/randomized...), ALPN, custom port, IP limit, speed limit, expiry, volume limit, subscription groups with public pages
- Live dashboard: connections, traffic chart, hourly usage, activity & error logs

## Environment Variables

| Variable | Purpose | Default |
|---|---|---|
| `PORT` | HTTP panel port | `8000` |
| `ADMIN_PASSWORD` | Panel password | `CYBERRAGE` |
| `SECRET_KEY` | Session/state signing key (auto-persisted) | auto |
| `DATA_DIR` | State persistence directory | `/data` |
| `RAILWAY_PUBLIC_DOMAIN` | Public hostname used in generated links | `localhost` |
| `TCP_PORT` | Raw VLESS TCP listener port | `8443` |
| `TLS_CERT` / `TLS_KEY` | PEM cert + key → TCP listener runs with TLS (`security=tls` in links) | *(off — plain TCP)* |

## Deploy

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --server-header=false
```

### VLESS + TCP on Railway / container hosts

The TCP listener binds on `TCP_PORT` (default `8443`) and is independent from the HTTP port.
- On a VPS: expose `TCP_PORT` directly (optionally set `TLS_CERT`/`TLS_KEY` for TLS).
- On Railway/Koyeb: add a TCP port mapping (`TCP_PORT`) to the service.
- For a CDN-bypass setup behind Cloudflare: set `RAILWAY_PUBLIC_DOMAIN` (or a reverse-proxy `X-Forwarded-Host`) to your domain and put clean IPs in the config's Clean IP Repository.

## Files

| File | Purpose |
|---|---|
| `main.py` | Panel, API, link generation, state management |
| `pages.py` | Single-file dashboard UI |
| `relay_vless.py` | WebSocket relay engine (VLESS header parse, quota batching) |
| `xhttp_siz10.py` | XHTTP packet-up / stream-up relay (sizing v10) |
| `tcp_vless.py` | Raw TCP VLESS listener (optional TLS) |
| `speed_limit.py` | Per-link adaptive speed throttling |
