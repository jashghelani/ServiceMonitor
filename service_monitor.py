import psutil
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import socket
import uuid

# Function to get the list of running services
def get_running_services():
    return [process.name() for process in psutil.process_iter(['name'])]

# Function to get the device's IP address
def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

# Function to get the device's MAC address
def get_mac_address():
    return ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])

# Function to send an email notification
def send_email(message):
    sender_email = "*******" #Sender Email
    receiver_email = "***********" #Receiver Email
    password = "*************" #Sender email password/passkey

    msg = MIMEText(message)
    msg['Subject'] = 'New Service Detected'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# Initial list of running services
initial_services = get_running_services()

# Continuously monitor for changes
while True:
    current_services = get_running_services()

    # Check for new services
    new_services = set(current_services) - set(initial_services)

    if new_services:
        # Get device information
        ip_address = get_ip_address()
        mac_address = get_mac_address()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Send a warning email with device information
        warning_message = (
            f"New service(s) detected: {', '.join(new_services)}\n"
            f"Device IP Address: {ip_address}\n"
            f"Device MAC Address: {mac_address}\n"
            f"Timestamp: {timestamp}"
        )
        send_email(warning_message)

    # Update the initial list for the next iteration
    initial_services = current_services
