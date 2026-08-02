
<p align="center">
  <a href="README.md"><b>English</b></a> &nbsp;|&nbsp; <a href="README.fa.md">فارسی</a>
</p>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=180&section=header&text=Cyber-Rage%20Multi%20Panel&fontSize=44&fontColor=ffffff&animation=fadeIn&fontAlignY=40" width="100%" />

# ⚡ Cyber-Rage Multi Panel

### 🌍 Multi-Country VLESS Gateway — One Public Port, Ten Countries

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&duration=2400&pause=900&color=8B5CF6&center=true&vCenter=true&width=640&lines=One+public+port+%E2%80%94+ten+country+exits;Tor-powered+IP+rotation+every+5+minutes;VLESS+%2B+WebSocket%2C+fully+automated;Deploy+in+minutes+on+any+Docker+host" alt="Typing animation" />

<br/>

[![Status](https://img.shields.io/badge/status-production--ready-brightgreen?style=for-the-badge&logo=checkmarx&logoColor=white&color=16a34a)](https://github.com/cyberrage-ananymus)
[![Port](https://img.shields.io/badge/public%20port-3000%20only-blue?style=for-the-badge&logo=server&logoColor=white&color=3b82f6)](https://github.com/cyberrage-ananymus)
[![Countries](https://img.shields.io/badge/countries-10%20configurable-orange?style=for-the-badge&logo=globe&logoColor=white&color=f59e0b)](https://github.com/cyberrage-ananymus)
[![Panel](https://img.shields.io/badge/panel-3x--ui%20v3.6.0-purple?style=for-the-badge&logo=nginx&logoColor=white&color=8b5cf6)](https://github.com/cyberrage-ananymus)
[![Tor](https://img.shields.io/badge/exit-Tor%20network-red?style=for-the-badge&logo=torproject&logoColor=white&color=d4545a)](https://github.com/cyberrage-ananymus)

<img src="https://profile-counter.glitch.me/cyber-rage-multi-panel/count.svg" alt="Visitor Counter" width="0" height="0" />

</div>

<br/>

> ### 🚀 **This revision fixes the root cause of the `address already in use` crash loop**
> The "direct" (non-Tor) inbound and nginx were both trying to bind **8080** while nginx *also* listened on 3000 — on single-port platforms that always caused a crash loop. Now **nginx is the ONLY process bound to `0.0.0.0`**, everything else binds `127.0.0.1` and is reverse-proxied.

---

## ✨ Why Cyber-Rage Multi Panel?

<table align="center">
<tr>
<td width="50%" align="center">

### 🚀 **Speed-Optimized**
- `OptimisticData` + reduced circuit build time for snappier tunnels
- `tcpFastOpen` + `tcpKeepAlive` on every inbound
- Streaming nginx proxy — **zero buffering**
- IP rotation every **5 minutes** per country

</td>
<td width="50%" align="center">

### 🛡️ **Privacy-First**
- Each country gets its **own isolated Tor instance**
- Exit pinned via `ExitNodes {cc}` + `StrictNodes 1`
- Oppressive-regime jurisdictions excluded by default
- **No "Tor" word anywhere in the panel**

</td>
</tr>
<tr>
<td width="50%" align="center">

### ⚙️ **Zero-Touch Automation**
- Automatic country **discovery & verification** (parallel, multi-provider)
- Automatic inbound/client/routing creation via 3x-ui API
- Failed countries get **no** inbound, no client, no routing
- Panel, links & status files auto-generated

</td>
<td width="50%" align="center">

### 🔀 **Multi-Country Routing**
- `/` → Direct (your server's own IP, **no Tor**)
- `/in1`…`/in10` → 10 different country exits
- Single public port **3000** — everything behind nginx
- Per-country **wrong-country self-heal** rotation

</td>
</tr>
</table>

---

## 📐 Architecture

```mermaid
flowchart LR
    subgraph Public["🌍 Public internet"]
        C[Client]
    end

    subgraph Container["Container — only port 3000 is exposed"]
        N["nginx :3000\n(the ONLY public bind)"]
        D["xray direct inbound\n127.0.0.1:8080"]
        P["3x-ui panel\n127.0.0.1:2053"]

        subgraph Countries["Per-country isolated stacks (verified only)"]
            direction TB
            I1["xray inbound /in1\n127.0.0.1:8081"] --> T1["Tor instance: de\nSOCKS 127.0.0.1:9052"]
            I2["xray inbound /in2\n127.0.0.1:8082"] --> T2["Tor instance: fr\nSOCKS 127.0.0.1:9053"]
        end

        N -->|"/"  "/direct"| D
        N -->|"/managepanel/"| P
        N -->|"/in1"| I1
        N -->|"/in2"| I2
    end

    C --> N
```

<details>
<summary><b>Why this fixes the "direct config doesn't work" problem</b> (click to expand)</summary>
<br/>

Before: `nginx` listened on `3000` **and** the xray direct inbound also tried to `listen 0.0.0.0:8080`. On a platform that only forwards **one** external port to your container, that second bind either failed or conflicted with nginx — the container crashed.

```
ERROR - XRAY: Failed to start: ... failed to listen on address: 0.0.0.0:8080
         ... bind: address already in use
```

After: `nginx` is the **only** process bound to `0.0.0.0`, on port `3000`. The direct inbound binds `127.0.0.1:8080` (loopback-only) and nginx's `/` and `/direct` locations reverse-proxy to it. Every other process — the panel, the Tor instances, the per-country inbounds — is also loopback-only.

</details>

---

## 🚀 Deployment

### 1️⃣ Clone & Deploy

```bash
# Any single-port container host: Railway, Koyeb, Render, Fly.io...
git clone https://github.com/x4gKing/3x-ui-multi.git
cd 3x-ui-multi
# Just point the platform at this repo — Dockerfile included!
```

### 2️⃣ Optional Environment Variables

| Variable | Purpose | Default |
|---|---|---|
| `XUI_USERNAME` | Panel username | `admin` |
| `XUI_PASSWORD` | Panel password | `admin` |
| `XUI_API_TOKEN` | Bearer token, skips form login if set | *(unset)* |
| `PUBLIC_DOMAIN` | Override auto-detected public domain | auto-detected |

> Everything else — public port, rotation interval, retry/timeout tuning, and the country list itself — lives in **`config.json`**.

---

## 📡 Endpoints

All endpoints are served on the **single public port (`3000`)** through nginx.

| Path | Type | Notes |
|---|---|---|
| `/` | 🌐 Direct | Default — server's own IP, no Tor |
| `/direct` | 🌐 Direct | Same as `/`, explicit path |
| `/in1` … `/in10` | 🔒 Country exit | Present **only if that country passed discovery** — see `config.json` for which path maps to which country |
| `/managepanel/` | — | 3x-ui admin panel |
| `/tor-status/all.json` | — | Live status for every configured country |
| `/tor-status/<code>.json` | — | Live status for one country (`exit_ip`, `verified`, `checked_at`, …) |
| `/health`, `/ping` | — | Liveness checks |

<details>
<summary>Default country list (10 configured in <code>config.json</code>)</summary>
<br/>

| Path | Country |
|---|---|
| `/in1` | 🇨🇦 Canada |
| `/in2` | 🇹🇷 Turkey |
| `/in3` | 🇩🇪 Germany |
| `/in4` | 🇫🇷 France |
| `/in5` | 🇸🇪 Sweden |
| `/in6` | 🇨🇭 Switzerland |
| `/in7` | 🇫🇮 Finland |
| `/in8` | 🇬🇧 United Kingdom |
| `/in9` | 🇪🇸 Spain |
| `/in10` | 🇷🇴 Romania |

Add, remove, or reassign any of these by editing the `tor.countries` array in `config.json` — nothing in the scripts is hardcoded to a specific list length or path.

</details>

---

## 🔎 How Country Discovery Works Now

```mermaid
sequenceDiagram
    participant S as start.sh
    participant T as Tor instance (per country)
    participant G as Geo-IP providers (×4)

    par all countries in parallel
        S->>T: launch + wait for Bootstrapped 100%
        loop up to verify_max_retries
            S->>T: fetch exit IP (×5 echo services, first valid wins)
            S->>G: resolve IP → country (first provider to answer wins)
            alt country matches
                S-->>S: ✅ verified, write status JSON
            else mismatch or lookup failed
                S->>T: SIGNAL NEWNYM (force new circuit)
                S-->>S: short bounded sleep, retry
            end
        end
    end
    S->>S: build VERIFIED_CODES[] from all status files
    S->>S: render nginx locations + hand off to panel-bootstrap.sh
```

Everything under `tor.*` in `config.json` is tunable without touching a script:

```jsonc
"tor": {
    "bootstrap_timeout": 240,     // max wait for Tor to reach 100%
    "verify_max_retries": 15,     // attempts to find a matching-country exit
    "verify_retry_sleep": 4,      // seconds between attempts
    "circuit_settle_sleep": 6,    // settle time after a fresh circuit
    "parallel_bootstrap": true,   // bootstrap + verify all countries at once
    "parallel_verify": true
}
```

---

## 🔁 Automatic IP Switching

Every **verified** country gets its own background rotation cycle (`tor.rotate_seconds`, default `300`s):

1. `SIGNAL NEWNYM` is sent to that country's own `ControlPort` — a fresh Tor circuit, and therefore a fresh exit IP, is requested.
2. The new exit IP is re-resolved through the same multi-provider geo-IP lookup used during discovery.
3. If the new IP is still in the correct country, the status file is updated and the client keeps working **uninterrupted**.
4. If the first rotation lands in the wrong country, one more attempt is made immediately; if that also fails, the country is marked unreachable until the *next* scheduled rotation (it is **not** torn down).

This runs entirely inside `start.sh` (`rotate_and_verify()`) — no external cron, no extra process.

---

## 🔒 Security & Naming

- **Direct connection** is the default on `/` and `/direct` — no Tor involved.
- **Country connections** are available on their `/inN` paths, but **only for countries that passed discovery**.
- **Strict exit-node enforcement** — each Tor instance is pinned with `ExitNodes {cc}` + `StrictNodes 1`; it is architecturally unable to exit anywhere else.
- **Excluded regions** — `tor.exclude_countries` in `config.json` (oppressive-regime and high-risk jurisdictions) are excluded from every instance's possible exit set, not just the target country's own.
- **No "Tor" in the panel** — inbound tags, remarks, outbound tags, and routing rules use only the country code/label. Panel screenshots, exported client links, and the xray JSON config never contain the word.
- **Nothing but nginx is public** — the panel, the direct inbound, every country inbound, and every Tor SOCKS/Control port bind to `127.0.0.1` only.

---

## 🚀 Speed Optimizations

This build includes targeted latency/throughput tweaks:

| Layer | Optimization |
|---|---|
| **Tor** | `OptimisticData 1`, `CircuitBuildTimeout 90`, `ConnectionPadding 0` (less overhead), `EnforceDistinctSubnets 1` |
| **Xray inbounds** | `tcpFastOpen: true`, `tcpKeepAlive: true` on every inbound stream |
| **Xray outbounds** | `tcpFastOpen` + `tcpKeepAlive` SOCKS outbounds to Tor |
| **nginx** | `proxy_buffering off`, `proxy_request_buffering off`, `tcp_nodelay`, `sendfile` |

---

## 📋 Logs

| File | Contents |
|---|---|
| `/var/log/panel-bootstrap.log` | Panel bootstrap: inbound/client/routing creation and teardown |
| `/var/log/tor/rotate.log` | Automatic IP-switching cycles |
| `/var/log/tor/<code>-stdout.log` | Raw stdout/stderr for that country's Tor process |
| `/var/log/tor/<code>/notices.log` | Tor notice-level log (bootstrap progress, circuit events) |
| `/var/log/tor/<code>/warnings.log` | Tor warning-level log |
| `/var/www/tor-status/<code>.json` | Live machine-readable status for that country |
| `/var/www/tor-status/all.json` | All countries combined |
| `/var/www/tor-status/setup-progress.json` | Overall `{total, verified, complete}` progress |

---

## 🗂️ File Map

```
.
├── Dockerfile               # Image build; only EXPOSEs port 3000 + healthcheck
├── config.json              # Single source of truth for ports, countries, tuning
├── nginx.conf.template      # Rendered at container start (envsubst + dynamic locations)
├── start.sh                 # Entrypoint: launches Tor, discovery, rotation, renders nginx, execs nginx
├── panel-bootstrap.sh       # Talks to the 3x-ui API: inbounds/clients/routing for verified countries
└── api-deploy-it-on-cloudflare.js  # Optional Cloudflare Worker: Tor/exit-IP checking + lookup API
```

---

## 📜 License & Credits

- **Panel:** [3x-ui](https://github.com/mhsanaei/3x-ui) — powerful xray management panel
- **Exit network:** [Tor Project](https://www.torproject.org/)
- **Branded & maintained by:** [Cyber-Rage](https://github.com/cyberrage-ananymus) ⚡

<div align="center">
<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer" width="100%" />

**⚡ Cyber-Rage Multi Panel — One port. Ten countries. Zero limits.**

</div>
