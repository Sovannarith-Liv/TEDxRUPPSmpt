import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase

EMAIL = "tedxrupp@gmail.com"
PASSWORD = "tedfeb2419"


def send_email(image_path, email):
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(EMAIL, PASSWORD)

    message = """Greeting from TEDxRUPP!

This is a confirmation email that we have received your payment.
You are now an official attendee of TEDxRUPPSalon that will be held on 27th September from 2PM - 5 PM at Factory Phnom Penh Theater.
 
Note: The registration will be opened from 1:30PM onwards. email(one ticket one email)

Below is your digital ticket QR code."""

    msg = MIMEMultipart("alternative")
    msg['Subject'] = "TEDxRUPP Salon ticket"
    msg['From'] = EMAIL
    msg['To'] = email
    msg.attach(MIMEText(message, "html"))
    image = open(image_path, "rb")
    image_attach = MIMEImage(image.read(), name="TEDxRUPP Salon Ticket")
    msg.attach(image_attach)
    server.sendmail(EMAIL, msg['To'], msg.as_string())
    print(email + " sent")
