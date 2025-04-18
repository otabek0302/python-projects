import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

print(f"Loaded EMAIL: {EMAIL}")
print(f"Loaded PASSWORD length: {len(PASSWORD) if PASSWORD else 'Not loaded'}")


def send_emails(recipients, send_count=1):
    """
    Send emails to multiple recipients multiple times.
    
    Args:
        recipients (list): List of email addresses to send to
        send_count (int): Number of times to send the message to each recipient
    """
    try:
        ob = smtplib.SMTP("smtp.gmail.com", 587)
        ob.ehlo()
        ob.starttls()
        ob.login(EMAIL, PASSWORD)

        subject = "Test Email"
        body = "This is a test email"

        for email in recipients:
            for i in range(send_count):
                msg = MIMEMultipart()
                msg['Subject'] = subject
                msg['From'] = EMAIL 
                msg['To'] = email
                msg.attach(MIMEText(body, 'plain'))

                ob.send_message(msg)
                print(f"✅ Email {i+1}/{send_count} sent to {email}")

        ob.quit()
        print(f"✅ All emails sent successfully! Total emails sent: {len(recipients) * send_count}")

    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed. Please check your email credentials.")
    except smtplib.SMTPException as e:
        print(f"❌ SMTP error: {str(e)}")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")

if __name__ == "__main__":
    recipients = ["muminovkjan@gmail.com", "muminovkjan@gmail.com", "muminovkjan@gmail.com"]
    send_count = 3  # Number of times to send to each recipient
    send_emails(recipients, send_count)