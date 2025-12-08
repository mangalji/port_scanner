# 🔍 Real-Time Port Scanner (Django + WebSockets + Nmap)

## 📌 Overview

This project is a **real-time network port scanner** built using **Django**, **Django Channels (WebSockets)**, and **Nmap**(nmap for accuracy). It allows users to scan single or multiple ports on any publicly accessible host and view results instantly in the browser — no page reloads required.

Traditional scanners run in the terminal, but this one provides a **web-based UI** with live streaming results, service detection, and timing metrics.

---

## 🚀 Features

- ⚡ Real-time port scanning output
- 🎯 Single port scan (fast and accurate)
- 🌐 Full port range scan (`-p-`)
- 🔍 Service & version detection (`-sV`)
- 🔁 Loader animation during scanning
- 🕒 Live scan timer
- 🧭 Asynchronous WebSocket-based updates
- 🖥️ Clean and responsive UI

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| Backend | Django, Django Channels, Python |
| Networking Engine | Nmap + python-nmap |
| Frontend | HTML, CSS, JavaScript |
| Real-time communication | WebSockets |
| Concurrency | ThreadPoolExecutor |

---

## 🎯 How It Works

1. User inputs a target host (e.g., `scanme.nmap.org`)
2. The frontend opens a WebSocket connection
3. The backend executes an Nmap scan asynchronously
4. Each discovered port is streamed live
5. The UI updates instantly with:
   - Port status (open/closed)
   - Service & version info
   - Timer until completion

> It's like running **Nmap in the browser**, visually and interactively.

---

## 🧪 Demo Output (Example)

```
⏱ Time: 11.7s
[OPEN] Port 22
Service: OpenSSH 8.9p1

[OPEN] Port 80
Service: Apache 2.4.58
```

---

## 📦 Installation & Setup

### 🔧 Requirements

- Python 3.10+
- Django
- Django Channels
- Nmap installed on system

### 📥 Install dependencies

```bash
sudo apt install nmap
pip install django channels python-nmap
```

or you can either use:

```bash
pip install -r requirements.txt
```

### ▶️ Run the project

```bash
python3 -m daphne -p 8000 port_scan.asgi:application
```

Open in your browser:

```
http://127.0.0.1:8000/
```

---

## 📂 Project Structure

```
/port_scanner_project
├── db.sqlite3
├── manage.py
├── port_scan
│   ├── asgi.py            # ASGI configuration for WebSockets
│   ├── settings.py        # Project settings
│   ├── urls.py            # Base URL routes
│   └── wsgi.py            # WSGI config
├── requirements.txt       # Python dependencies
└── scanner
    ├── consumers.py       # WebSocket handler + scanning logic
    ├── routing.py         # WebSocket routing
    ├── views.py           # HTTP views (if needed)
    ├── models.py          # App models (not used in this project)
    ├── admin.py
    ├── apps.py
    ├── tests.py
    ├── templates
    │   └── index.html     # Main UI page
```

---

## 🚧 Future Enhancements

- 📤 Export scan results (CSV)
- 📊 Graphical progress bar
- 🛡️ OS fingerprinting (`-O`) — requires sudo
- 📁 Save scan history

---

## 📌 Why This Project Is Valuable

This project demonstrates:

- Real-time async programming
- WebSockets integration
- Nmap automation
- Network security fundamentals
- Clean full-stack design

Perfect for **resume**, **portfolio**, and **security-related interviews**.

---

## 👤 Author

**Raj Mangal**  
A developer exploring the intersection of networking, automation, and web technologies.

---

## 📜 License

This project is open under the **MIT License**.  
Feel free to use, modify, or extend it.

---

### ⭐ If this project helped you, consider giving it a GitHub star!
