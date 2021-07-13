import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import os
import time
import threading

class sendMail(threading.Thread):
    def __init__(self, subject, message, to):
        threading.Thread.__init__(self)
        self.event = threading.Event()
        self.subject = subject
        self.message = message
        self.receivers = receivers

    def run(self):
    
        #The mail addresses and password
        sender_address = "<senders-mail>"
        sender_pass = "<senders-password>"

        #Setup the MIME
        mail = MIMEMultipart()
        mail['From'] = sender_address
        mail['To'] = ", ".join(self.receivers)
        mail['Subject'] = self.subject

        mail.attach(MIMEText(self.message,'plain'))

        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = mail.as_string()
        session.sendmail(sender_address, self.receivers, text)
        session.quit()
        print('Mail Sent')


message = 'Hello,this is a test mail.'
subject = "Test"
receivers = ["<receiver-mail1>", "<receiver-mail2>", "<receiver-mail3>"]
sendMail(subject, message, receivers).start()