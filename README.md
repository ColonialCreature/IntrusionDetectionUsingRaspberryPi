# 🚨 Smart Intrusion Detection System

An IoT-powered security system built with **Raspberry Pi**, **PIR Sensor**, and **Pi Camera**. It detects motion, captures real-time images, and instantly notifies the owner via email. This project demonstrates the power of Python, computer vision, and embedded systems in building practical home security solutions.

---

## 📷 Project Overview

- 📡 Detects motion using a Passive Infrared (PIR) sensor
- 📸 Captures images/videos with Pi Camera on detection
- 📧 Sends email alerts with attached intruder images
- 📊 Logs intrusion events with timestamps
- 🧠 Built with Python, OpenCV, smtplib, and GPIO libraries

---

## 🧰 Tech Stack

Tech Description

1. Raspberry Pi 3B - Core platform for processing and sensor control
2. Python - Scripting and automation
3. OpenCV - Image capture and processing
4. smtplib - Email notifications
5. RPi.GPIO - Sensor integration via GPIO pins
6. Raspbian OS - Operating system running on Pi

---

## 🛠️ Setup & Usage

1. **Clone the Repository** 
   ```bash
   git clone https://github.com/yourusername/smart-intrusion-system.git
   cd smart-intrusion-system
2. **Install Dependencies**
    ```
    sudo apt update
    sudo apt install python3-opencv
    pip3 install RPi.GPIO
4. **Update Email Credentials in main.py**
    ```
    SMTP_USERNAME = 'your_email@gmail.com'
    SMTP_APP_PASSWORD = 'your_app_password'
    RECIPIENT_EMAIL = 'destination_email@example.com'
5. **Run the Script**
    ```
    python3 main.py

---

🖼️ Sample Output

---

🌱 Future Enhancements

 - Web dashboard for real-time video feed
 - Telegram/SMS integration
 - Night vision camera support
 - AI-based object detection with TensorFlow

---

👤 Author
**Aryan Deshmukh**
