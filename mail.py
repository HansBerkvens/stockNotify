import smtplib
from email.mime.text import MIMEText
import os

pw = os.getenv('STOCK_NOTIFY_EMAIL_PASSWORD')
recipient = os.getenv('RECIPIENT')

def send_notification(subject: str, body: str):
    sender = os.environ["GMAIL_ADDRESS"]
    password = os.environ["STOCK_NOTIFY_EMAIL_PASSWORD"]
    recipient = os.environ.get("RECIPIENT")  # send to yourself, or set a separate recipient

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)


if __name__ == '__main__':
    send_notification('Test subject', 'Stocks man')