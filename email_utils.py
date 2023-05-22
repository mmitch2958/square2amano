import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
import base64

def send_qr_code_email(email, qr_code_number):
    # Define your email configuration
    from_email = mike.mitchell@psxgroup.com
    to_email = email
    subject = 'Your QR Code for Validation'
    
    # Email content (HTML)
    html_content = f"""
    <html>
        <body>
            <h1>Your QR Code for Validation</h1>
            <p>QR Code Number: {qr_code_number}</p>
            <img src="data:image/png;base64,{qr_code_number}" alt="QR Code">
        </body>
    </html>
    """

    # Create email message
    msg = MIMEMultipart('related')
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(html_content, 'html'))

    # Send email
    with smtplib.SMTP(smtp.gmail.com, 587) as server:  # Replace 'smtp.example.com' and 587 with your SMTP server and port
        server.starttls()
        server.login(from_email, EMAIL_PASSWORD=dvvukbnjcjxpdpic)  # Replace 'your_email_password' with your actual email password
        server.sendmail(from_email, to_email, msg.as_string())

