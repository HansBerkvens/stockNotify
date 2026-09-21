import smtplib
from email.mime.text import MIMEText
import os
import logging
logging.basicConfig(level=logging.INFO, format="%(name)s:%(levelname)s:%(asctime)s\t\t%(message)s", datefmt="%H:%M:%S", force=True)

logging.info('At least the logger works (mail)')


def send_notification(subject: str, body: str):
    sender = os.environ["GMAIL_ADDRESS"]
    password = os.environ["STOCK_NOTIFY_EMAIL_PASSWORD"]
    recipient = os.environ.get("RECIPIENT")

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        logging.info(f'Sending mail {subject = }:: {body}')
        server.login(sender, password)
        server.send_message(msg)


if __name__ == '__main__':
    send_notification('Test subject', 'Stocks man')