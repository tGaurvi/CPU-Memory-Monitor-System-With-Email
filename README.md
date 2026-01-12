# CPU-Memory-Monitor-System-With-Email

A lightweight Python script designed to monitor critical system resources and send automated alerts via the SMTP protocol.

## 📋 Features
* **Real-time Monitoring:** Tracks CPU utilization and memory availability using the `psutil` library.
* **Custom Thresholds:** Allows users to define specific limits for hardware usage.
* **Automated Alerts:** Sends instant email notifications to administrators when thresholds are exceeded.
* **Simple Integration:** Uses the standard SMTP protocol for broad compatibility with email providers like Gmail or Outlook.

## 🛠️ Built With
* [Python 3](www.python.org)
* [psutil](psutil.readthedocs.io) - Cross-platform library for retrieving system information.
* [smtplib](docs.python.org) - Python's built-in module for sending emails.

## 🚀 Getting Started

### Prerequisites
* Python 3.x installed.
* An email account with SMTP access (e.g., Gmail App Password).

### Installation
1. **Clone the repository:**
   ```bash
   git clone github.com
   cd YOUR_REPO_NAME
