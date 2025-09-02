import logging
import argparse

# Files
root_files = './files/'

# Log files
log_file = root_files + 'log.txt'

# Debug
dry_run = False

'''
Send an email
'''
def send_mail(args):
    print("Send mail")
    return 0
'''
Co Pilot
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("This is the email body")
msg["Subject"] = "Your Subject"
msg["From"] = "your_email@example.com"
msg["To"] = "recipient@example.com"

# For Gmail, use smtp.gmail.com and port 587
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()
    smtp.login("your_email@example.com", "your_password")
    smtp.send_message(msg)

Grok

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Enable TLS for security
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(msg)
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error sending email: {e}")

    finally:
        server.quit()

# Example usage
sender = "your_email@gmail.com"
password = "your_app_specific_password"  # Use an App Password for Gmail
recipient = "recipient@example.com"
subject = "Test Email"
body = "This is a test email sent from Python!"

send_email(sender, password, recipient, subject, body)

Gemini

import smtplib
from email.message import EmailMessage
from pathlib import Path

# Set up the email content
msg = EmailMessage()
msg['Subject'] = 'Email with an Attachment'
msg['From'] = 'your_email@gmail.com'
msg['To'] = 'recipient_email@example.com'
msg.set_content('This email includes a document attached below.')

# Add a file as an attachment
file_path = Path('document.pdf')
with open(file_path, 'rb') as f:
    file_data = f.read()
    file_name = file_path.name
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

# SMTP server configuration (same as above)
smtp_server = 'smtp.gmail.com'
smtp_port = 465
email_address = 'your_email@gmail.com'
email_password = 'your_app_password'

try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
    print("Email with attachment sent successfully!")
except Exception as e:
    print(f"Error: {e}")
    
'''

def setup_debug(): 
    logger = logging.getLogger("")
    logging.basicConfig(level=logging.DEBUG)
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s %(levelname)s : %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='VolMail',
                                        description='These function allow the user to send an email',
                                        epilog='See "%(prog)s help COMMAND" for help on a specific command.')
    parser.add_argument('--debug', '-d', action='count', help='Print debug output')
    parser.add_argument('--dry-run', '-dr', action='count', help='Execute a dry run')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    send_parser = subparsers.add_parser('send', help='Send an email')
    send_parser.set_defaults(func=send_mail)

    args = parser.parse_args()

    if args.debug:
        setup_debug()

    if args.dry_run:
        dry_run = True

    if args.command:
        args.func(args)
    else:
        parser.print_help()
