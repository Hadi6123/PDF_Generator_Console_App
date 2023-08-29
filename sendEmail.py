import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import sys


class SendEmail:
    def __init__(self):
        pass
    
    def email_send(self, address, pdf):
        subject = "An email with attachment from Python"
        body = "This is an email with attachment sent from Python"

        username = "hadiisb6i@gmail.com"
        password = "gqtkpvyultpdyltd"
        receiver = address

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = username
        message["To"] = receiver
        message["Subject"] = subject
        message["Bcc"] = receiver  # Recommended for mass emails

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        filename = pdf # In same directory as script

        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, text)
            
if __name__ == '__main__':
    email = SendEmail()
    #email.email_send("hadiisb6i@gmail.com", "GeneratedPDFS/output.pdf")