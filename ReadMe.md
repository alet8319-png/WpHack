# 🔐 WPHACK WordPress Authentication Security Tester

<div align="center">

**A focused WordPress penetration testing utility for authorized penetration testers assessments**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-Join%20Channel-26A5E4)](https://t.me/jundalnabi)

</div>

---

## 📋 Overview

**WPHACK** is a professional WordPress authentication testing tool designed for authorized penetration testers and security researchers. It assists in identifying weak credentials during red team engagements and security audits by systematically testing authentication vectors against WordPress installations.

---

---

## 📋 Description

**How to use this tool** I am testing this across multiple browsers. If the script does not work on your end, please let me know or DM me for the test code. This task might take some time, depending on your OSINT skills.First, use WPScan to find the WordPress admin usernames. Next, add the discovered username to the wphack.py script. If you are on Windows, open the file using VS Code or Notepad. If you are on Linux, simply run nano wphack.py. Locate the line that reads USERNAME = "example" and replace "example" with your target username.Next, you need to set up and run the tool. I have included a virtual environment folder. Run source wphack/bin/activate to start it. If you do not see the wphack folder, create your own virtual environment by running python -m venv wphack, and then activate it using source wphack/bin/activate. If you create a custom folder name, just remember to use that name in the activation command.Finally, if you had to create a fresh virtual environment instead of using the pre-configured one, make sure to install the dependencies first by running pip install -r requirements.txt. Once that is done, run the tool and it should work properly.

---

## ✅ Intended Use

This tool is intended **only** for:

- Authorized penetration tests with explicit written permission
- Security audits of systems you own or are contracted to test
- Educational environments (CTFs, labs, personal studies)
- Bug bounty programs with clear scope boundaries

> You have confirmed you are authorized to perform this penetration test. Proceed with professional responsibility.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **WPScan Integration** | Works alongside WPScan for initial username and password enumeration |
| **Cross-Browser Compatible** | Tested across Chrome, Firefox, Edge, and Safari |
| **Configurable Target** | Simple inline configuration for target username and password |
| **Cross-Platform** | Fully functional on Linux, Windows, and macOS |
| **Virtual Environment** | Isolated Python environment for clean dependency management |

---

## 🔧 Prerequisites

| Tool | Version | Installation |
|------|---------|-------------|
| **Python** | 3.8+ | [python.org/downloads](https://python.org/downloads) |
| **WPScan** | Latest | `gem install wpscan` or `apt install wpscan` (Kali) |
| **pip** | Latest | Bundled with Python 3.8+ |

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/alet8319-png/WpHack.git
cd WpHack

python -m venv wphack
source wphack/bin/activate

pip install -r requirements.txt

python wphack.py