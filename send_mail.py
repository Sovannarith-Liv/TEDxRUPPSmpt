import smtplib, os, csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from threading import Thread


class EmailThread(Thread):
    def __init__(self, email_to, csv, image):
        self.email_to = email_to
        self.image = image 
        Thread.__init__(self)


    def run (self):
        msg = MIMEMultipart("alternative")
        message = "Hello welcome!"
        password = os.environ.get('EMAIL_PASS')
        
        msg['Subject'] = "Testing"
        msg['From'] = os.environ.get('EMAIL_USER')
        msg['To'] = self.email_to

        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(msg['From'], password)
        msg.attach(MIMEText(message, "html"))
        
        #add the csv file in the email body
        """part = MIMEBase('application', "octet-stream")
        part.set_payload(csv.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename='aud.csv')
        msg.attach(part)"""


        msg.attach(MIMEImage(self.image.read()))
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()

        print("Email was send successfully")

#read the csv file row by row 
"""with open('./static/aud.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)"""
        
