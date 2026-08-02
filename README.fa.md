<p align="center" dir="ltr">
  <a href="README.md"><b>English</b></a> &nbsp;|&nbsp; <a href="README.fa.md">فارسی</a>
</p>

<div align="center" dir="rtl">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=180&section=header&text=%F0%9F%94%A5%20Cyber-Rage%20Multi%20Panel&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=42" width="100%" />

# ⚡ سایبر ریج مالتـی پنـل (Cyber-Rage Multi Panel)

### 🌍 دروازه‌ی چندکشوری VLESS — یک پورت عمومی، ده کشور

<img src="https://readme-typing-svg.demolab.com?font=Vazirmatn&size=16&duration=2400&pause=900&color=8B5CF6&center=true&vCenter=true&width=640&lines=%DB%8C%DA%A9%20%D9%BE%D9%88%D8%B1%D8%AA%D8%8C%20%D8%AF%D9%87%20%DA%A9%D8%B4%D9%88%D8%B1%20%D8%AE%D8%B1%D9%88%D8%AC%DB%8C;%D8%AA%D8%B9%D9%88%DB%8C%D8%B6%20%D8%AE%D9%88%D8%AF%DA%A9%D8%A7%D8%B1%20%D8%A2%DB%8C%E2%80%8C%D9%BE%DB%8C%20%D9%87%D8%B1%205%20%D8%AF%D9%82%DB%8C%D9%82%D9%87;%D8%B3%D8%B1%DB%8C%D8%B9%D8%AA%20%D8%A8%D8%A7%D9%84%D8%A7%20%D8%A8%D8%A7%20%D8%AA%D9%86%D8%B8%DB%8C%D9%85%D8%A7%D8%AA%20%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%DB%8C;%D8%B1%D8%A7%D9%87%E2%80%8C%D8%A7%D9%86%D8%AF%D8%A7%D8%B2%DB%8C%20%D8%AF%D8%B1%20%DA%86%D9%86%D8%AF%20%D8%AF%D9%82%DB%8C%D9%82%D9%87" alt="انیمیشن تایپ" />

<br/>

[![وضعیت](https://img.shields.io/badge/%D9%88%D8%B6%D8%B9%DB%8C%D8%AA-%D8%A2%D9%85%D8%A7%D8%AF%D9%87_%D8%AA%D9%88%D9%84%DB%8C%D8%AF-brightgreen?style=for-the-badge&logo=checkmarx&logoColor=white&color=16a34a)](https://github.com/cyberrage-ananymus)
[![پورت عمومی](https://img.shields.io/badge/%D9%BE%D9%88%D8%B1%D8%AA-%D9%81%D9%82%D8%B7_3000-blue?style=for-the-badge&logo=server&logoColor=white&color=3b82f6)](https://github.com/cyberrage-ananymus)
[![کشورها](https://img.shields.io/badge/%DA%A9%D8%B4%D9%88%D8%B1%D9%87%D8%A7-10_%D9%82%D8%A7%D8%A8%D9%84_%D8%AA%D9%86%D8%B8%DB%8C%D9%85-orange?style=for-the-badge&logo=globe&logoColor=white&color=f59e0b)](https://github.com/cyberrage-ananymus)
[![پنل](https://img.shields.io/badge/%D9%BE%D9%86%D9%84-3x--ui_v3.6.0-purple?style=for-the-badge&logo=nginx&logoColor=white&color=8b5cf6)](https://github.com/cyberrage-ananymus)
[![خروجی](https://img.shields.io/badge/%D8%AE%D8%B1%D9%88%D8%AC%DB%8C-%D8%B4%D8%A8%DA%A9%D9%87_%D8%AA%D9%88%D8%B1-red?style=for-the-badge&logo=torproject&logoColor=white&color=d4545a)](https://github.com/cyberrage-ananymus)

</div>

<br/>

> ### 🚀 **این نسخه ریشه‌ی مشکل crash-loop «address already in use» را حل می‌کند**
> اینباند «مستقیم» (غیر تور) و nginx هر دو سعی می‌کردند پورت **8080** را بگیرند در حالی که nginx روی 3000 هم گوش می‌داد — روی پلتفرم‌های تک‌پورتی این همیشه باعث crash-loop می‌شد. حالا **فقط nginx به `0.0.0.0` متصل است** و بقیه روی `127.0.0.1` بایند شده و از پشت nginx پراکسی می‌شوند.

---

## ✨ چرا سایبر ریج مالتـی پنـل؟

<table align="center" dir="rtl">
<tr>
<td width="50%" align="center">

### 🚀 **بهینه‌شده برای سرعت**
- `OptimisticData` + زمان ساخت مدار کمتر برای تونل روان‌تر
- `tcpFastOpen` + `tcpKeepAlive` روی همه اینباندها
- پراکسی استریمینگ nginx — **بدون بافرینگ**
- تعویض آی‌پی هر **۵ دقیقه** برای هر کشور

</td>
<td width="50%" align="center">

### 🛡️ **حریم خصوصی در اولویت**
- هر کشور **نشست تور ایزوله‌ی خودش** را دارد
- خروجی با `ExitNodes {cc}` + `StrictNodes 1` قفل شده
- کشورهای پرخطر به‌صورت پیش‌فرض حذف شده‌اند
- **هیچ‌جای پنل کلمه‌ی «تور» دیده نمی‌شود**

</td>
</tr>
<tr>
<td width="50%" align="center">

### ⚙️ **اتوماسیون کامل**
- کشف و تأیید خودکار کشور (موازی، چندمنبعی)
- ساخت خودکار اینباند/کلاینت/مسیریابی با API پنل 3x-ui
- کشورهای ناموفق **هیچ** اینباند/کلاینتی نمی‌گیرند
- لینک‌ها، پنل و فایل‌های وضعیت خودکار ساخته می‌شوند

</td>
<td width="50%" align="center">

### 🔀 **مسیریابی چندکشوری**
- `/` → مستقیم (آی‌پی خود سرور، **بدون تور**)
- `/in1`…`/in10` → ۱۰ خروجی از کشورهای مختلف
- فقط یک پورت عمومی **3000** — همه‌چیز پشت nginx
- چرخش خودکار با **خوداصلاحی کشوری**

</td>
</tr>
</table>

---

## 📐 معماری

```mermaid
flowchart LR
    subgraph Public["🌍 اینترنت عمومی"]
        C[کلاینت]
    end

    subgraph Container["کانتینر — فقط پورت 3000 باز است"]
        N["nginx :3000 (تنها اتصال عمومی)"]
        D["xray اینباند مستقیم 127.0.0.1:8080"]
        P["پنل 3x-ui 127.0.0.1:2053"]

        subgraph Countries["نشست‌های ایزوله هر کشور (فقط تأییدشده‌ها)"]
            direction TB
            I1["xray اینباند /in1 127.0.0.1:8081"] --> T1["نشست تور: de SOCKS 127.0.0.1:9052"]
            I2["xray اینباند /in2 127.0.0.1:8082"] --> T2["نشست تور: fr SOCKS 127.0.0.1:9053"]
        end

        N -->|"/"  "/direct"| D
        N -->|"/managepanel/"| P
        N -->|"/in1"| I1
        N -->|"/in2"| I2
    end

    C --> N
```

<details>
<summary><b>چرا این مشکل «کانفیگ مستقیم کار نمی‌کند» را حل می‌کند؟</b> (برای باز کردن کلیک کنید)</summary>
<br/>

قبلش: `nginx` روی `3000` گوش می‌داد **و** اینباند مستقیم xray هم سعی می‌کرد روی `0.0.0.0:8080` بایند شود. روی پلتفرمی که فقط **یک** پورت خارجی به کانتینر شما می‌دهد، این بایند دوم یا خطا می‌داد یا با nginx تداخل می‌کرد — کانتینر کرش می‌کرد.

```
ERROR - XRAY: Failed to start: ... failed to listen on address: 0.0.0.0:8080
         ... bind: address already in use
```

حالا: `nginx` **تنها** پروسه‌ای است که روی `0.0.0.0` (پورت `3000`) بایند شده. اینباند مستقیم روی `127.0.0.1:8080` (فقط لوپ‌بک) بایند می‌شود و لوکیشن‌های `/` و `/direct` در nginx به آن پراکسی می‌دهند. بقیه پروسه‌ها — پنل، نشست‌های تور و اینباندهای کشوری — همگی فقط لوپ‌بک هستند.

</details>

---

## 🚀 نصب و راه‌اندازی

### 1️⃣ کلون و دیپلوی

```bash
# روی هر هاست تک‌پورتی: Railway، Koyeb، Render، Fly.io و...
git clone https://github.com/x4gKing/3x-ui-multi.git
cd 3x-ui-multi
# کافیه این ریپو رو به پلتفرم بدید — Dockerfile داخلش هست!
```

### 2️⃣ متغیرهای محیطی اختیاری

| متغیر | کاربرد | پیش‌فرض |
|---|---|---|
| `XUI_USERNAME` | نام کاربری پنل | `admin` |
| `XUI_PASSWORD` | رمز پنل | `admin` |
| `XUI_API_TOKEN` | توکن Bearer، ورود با فرم را دور می‌زند | *(تنظیم‌نشده)* |
| `PUBLIC_DOMAIN` | جایگزینی دامنه‌ی خودکار شناسایی‌شده | شناسایی خودکار |

> بقیه تنظیمات — پورت عمومی، فاصله‌ی چرخش، تایم‌اوت‌ها و لیست کشورها — همه در **`config.json`** است.

---

## 📡 اندپوینت‌ها

همه اندپوینت‌ها روی **یک پورت عمومی (`3000`)** از طریق nginx سرو می‌شوند.

| مسیر | نوع | توضیحات |
|---|---|---|
| `/` | 🌐 مستقیم | پیش‌فرض — آی‌پی خود سرور، بدون تور |
| `/direct` | 🌐 مستقیم | همان `/` با مسیر صریح |
| `/in1` … `/in10` | 🔒 خروجی کشوری | فقط اگر آن کشور در کشف تأیید شده باشد — نگاشت مسیر به کشور در `config.json` |
| `/managepanel/` | — | پنل مدیریت 3x-ui |
| `/tor-status/all.json` | — | وضعیت زنده همه کشورها |
| `/tor-status/<code>.json` | — | وضعیت زنده یک کشور (`exit_ip`، `verified`، `checked_at` و…) |
| `/health`, `/ping` | — | بررسی سلامت |

<details>
<summary>لیست پیش‌فرض کشورها (۱۰ کشور در <code>config.json</code>)</summary>
<br/>

| مسیر | کشور |
|---|---|
| `/in1` | 🇨🇦 کانادا |
| `/in2` | 🇹🇷 ترکیه |
| `/in3` | 🇩🇪 آلمان |
| `/in4` | 🇫🇷 فرانسه |
| `/in5` | 🇸🇪 سوئد |
| `/in6` | 🇨🇭 سوئیس |
| `/in7` | 🇫🇮 فنلاند |
| `/in8` | 🇬🇧 بریتانیا |
| `/in9` | 🇪🇸 اسپانیا |
| `/in10` | 🇷🇴 رومانی |

هر کدام را می‌توانید با ویرایش آرایه‌ی `tor.countries` در `config.json` اضافه/حذف/جابجا کنید — هیچ‌کدام از اسکریپت‌ها به طول یا مسیر خاصی وابسته نیستند.

</details>

---

## 🔎 فرایند کشف کشورها

```mermaid
sequenceDiagram
    participant S as start.sh
    participant T as نشست تور (هر کشور)
    participant G as سرویس‌های Geo-IP (×۴)

    par همه کشورها به‌صورت موازی
        S->>T: راه‌اندازی + انتظار برای Bootstrapped 100%
        loop تا verify_max_retries بار
            S->>T: دریافت آی‌پی خروجی (×۵ سرویس، اولین معتبر برنده است)
            S->>G: تبدیل آی‌پی به کشور (اولین سرویس پاسخ‌دهنده)
            alt کشور منطبق شد
                S-->>S: ✅ تأیید شد، نوشتن وضعیت JSON
            else عدم تطابق یا خطای جستجو
                S->>T: SIGNAL NEWNYM (مدار جدید اجباری)
                S-->>S: مکث کوتاه و تلاش دوباره
            end
        end
    end
    S->>S: ساخت VERIFIED_CODES[] از فایل‌های وضعیت
    S->>S: رندر لوکیشن‌های nginx + تحویل به panel-bootstrap.sh
```

همه‌چیز زیر کلید `tor.*` در `config.json` بدون دست زدن به اسکریپت قابل تنظیم است:

```jsonc
"tor": {
    "bootstrap_timeout": 240,     // حداکثر انتظار برای رسیدن تور به 100%
    "verify_max_retries": 15,     // تلاش برای پیدا کردن خروجی با کشور درست
    "verify_retry_sleep": 4,      // ثانیه بین تلاش‌ها
    "circuit_settle_sleep": 6,    // زمان نشستن بعد از مدار تازه
    "parallel_bootstrap": true,   // راه‌اندازی و تأیید همه کشورها همزمان
    "parallel_verify": true
}
```

---

## 🔁 تعویض خودکار آی‌پی

هر کشور **تأییدشده** چرخه‌ی چرخش پس‌زمینه‌ی خودش را دارد (`tor.rotate_seconds`، پیش‌فرض `300` ثانیه):

1. `SIGNAL NEWNYM` به `ControlPort` همان کشور فرستاده می‌شود — مدار تور تازه، یعنی آی‌پی خروجی تازه.
2. آی‌پی خروجی جدید با همان جستجوی چندمنبعی Geo-IP دوباره بررسی می‌شود.
3. اگر آی‌پی جدید هنوز در کشور درست باشد، فایل وضعیت به‌روز می‌شود و کلاینت **بدون قطعی** کار می‌کند.
4. اگر چرخش اول به کشور اشتباه برود، یک بار دیگر بلافاصله تلاش می‌شود؛ اگر باز هم نشد، کشور تا چرخش بعدی «غیرقابل دسترس» علامت می‌خورد (حذف **نمی‌شود**).

این کار کاملاً داخل `start.sh` انجام می‌شود (`rotate_and_verify()`) — بدون cron خارجی، بدون پروسه‌ی اضافه.

---

## 🔒 امنیت و نام‌گذاری

- **اتصال مستقیم** پیش‌فرض روی `/` و `/direct` است — بدون تور.
- **اتصالات کشوری** روی مسیرهای `/inN` در دسترس‌اند، اما **فقط برای کشورهایی که کشف را رد کرده‌اند**.
- **اجرای سخت‌گیرانه‌ی خروجی** — هر نشست تور با `ExitNodes {cc}` + `StrictNodes 1` قفل شده؛ از نظر معماری نمی‌تواند از جای دیگری خارج شود.
- **مناطق حذف‌شده** — `tor.exclude_countries` در `config.json` (کشورهای دارای محدودیت و پرخطر) از خروجی همه نشست‌ها حذف شده‌اند.
- **بدون «تور» در پنل** — تگ‌ها، رمارک‌ها، اوت‌باندها و قوانین مسیریابی فقط کد/نام کشور را دارند. اسکرین‌شات‌ها، لینک‌های کلاینت و کانفیگ JSON xray هرگز شامل این کلمه نیستند.
- **فقط nginx عمومی است** — پنل، اینباند مستقیم، همه اینباندهای کشوری و همه پورت‌های SOCKS/Control تور فقط روی `127.0.0.1` بایند شده‌اند.

---

## 🚀 بهینه‌سازی‌های سرعت

این نسخه شامل تنظیمات هدفمند تأخیر و پهنای باند است:

| لایه | بهینه‌سازی |
|---|---|
| **تور** | `OptimisticData 1`، `CircuitBuildTimeout 90`، `ConnectionPadding 0` (سربار کمتر)، `EnforceDistinctSubnets 1` |
| **اینباندهای Xray** | `tcpFastOpen: true`، `tcpKeepAlive: true` روی استریم همه اینباندها |
| **اوت‌باندهای Xray** | اوت‌باندهای SOCKS با `tcpFastOpen` + `tcpKeepAlive` به سمت تور |
| **nginx** | `proxy_buffering off`، `proxy_request_buffering off`، `tcp_nodelay`، `sendfile` |

---

## 📋 لاگ‌ها

| فایل | محتوا |
|---|---|
| `/var/log/panel-bootstrap.log` | راه‌اندازی پنل: ساخت/حذف اینباند، کلاینت و مسیریابی |
| `/var/log/tor/rotate.log` | چرخه‌های تعویض خودکار آی‌پی |
| `/var/log/tor/<code>-stdout.log` | خروجی خام آن کشور از فرایند تور |
| `/var/log/tor/<code>/notices.log` | لاگ اطلاع‌رسانی تور (پیشرفت بوت‌استرپ، رویدادهای مدار) |
| `/var/log/tor/<code>/warnings.log` | لاگ هشدارهای تور |
| `/var/www/tor-status/<code>.json` | وضعیت زنده و قابل‌خواندن ماشینی آن کشور |
| `/var/www/tor-status/all.json` | همه کشورها با هم |
| `/var/www/tor-status/setup-progress.json` | پیشرفت کلی `{total, verified, complete}` |

---

## 🗂️ ساختار فایل‌ها

```
.
├── Dockerfile               # ساخت ایمج؛ فقط پورت 3000 را EXPOSE می‌کند + healthcheck
├── config.json              # منبع واحد حقیقت برای پورت‌ها، کشورها و تنظیمات
├── nginx.conf.template      # در شروع کانتینر رندر می‌شود (envsubst + لوکیشن‌های داینامیک)
├── start.sh                 # نقطه ورود: اجرای تور، کشف، چرخش، رندر nginx و اجرای nginx
├── panel-bootstrap.sh       # ارتباط با API پنل 3x-ui: اینباند/کلاینت/مسیریابی کشورهای تأییدشده
└── api-deploy-it-on-cloudflare.js  # Worker اختیاری Cloudflare: بررسی تور/آی‌پی خروجی + API جستجو
```

---

## 📜 لایسنس و قدردانی

- **پنل:** [3x-ui](https://github.com/mhsanaei/3x-ui) — پنل مدیریت قدرتمند xray
- **شبکه خروجی:** [پروژه تور](https://www.torproject.org/)
- **برند و نگهداری:** [Cyber-Rage](https://github.com/cyberrage-ananymus) ⚡

<div align="center">
<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer" width="100%" />

**⚡ سایبر ریج مالتـی پنـل — یک پورت. ده کشور. بدون محدودیت.**

</div>
