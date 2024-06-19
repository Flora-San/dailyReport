import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time


# Function to send email
def send_email():
    # Email credentials
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    recipient_email = "recipient_email@example.com"

    # Email content
    subject = "Daily Report"
    body = "This is your daily report."

    # Setting up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    # Attach the body with the msg instance
    message.attach(MIMEText(body, 'plain'))

    # Create SMTP session for sending the mail
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        server.starttls()  # enable security
        server.login(sender_email, sender_password)  # login with mail_id and password
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()


# Schedule the email to be sent daily
schedule.every().day.at("09:00").do(send_email)  # Set the time as per your requirement

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # wait one minute
