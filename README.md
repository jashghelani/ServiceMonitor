# ServiceMonitor
Service Monitor: Python script for real-time monitoring of running services and email notifications for new detections.

Service Monitor
Description
This Python script continuously monitors running services on a device and sends email notifications when new services are detected. It retrieves information about the device's IP address and MAC address to include in the notification email.

Prerequisites
Python 3.x
psutil library (pip install psutil)
smtplib library (built-in)
email library (built-in)
socket library (built-in)
uuid library (built-in)

Usage
Ensure that Python 3.x is installed on your system.
Install the required libraries by running:
pip install psutil
Replace the placeholder values (sender_email, receiver_email, password) in the script with your actual email credentials.
Run the script using the following command:
python service_monitor.py

Configuration
Modify the sender_email, receiver_email, and password variables in the script to match your email credentials.
Adjust the email server settings (smtp.gmail.com, 587) if you are using a different email provider.

Note
This script is designed to run continuously in the background. Ensure proper permissions and considerations for running scripts on your device.
