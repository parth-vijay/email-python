import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import os
import time

# time.sleep(6)
mail_content = "Hello, This is a test mail."

#The mail addresses and password
sender_address = "<senders-mail>"
sender_pass = "<senders-password>"
receiver_address = "<receiver-mail>"
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Warning'

## Send Text in E-Mail:
message.attach(MIMEText(mail_content, 'plain'))

## Send Image in E-Mail:
fp = open("/home/parth/Pictures/pendrive/image.png", 'rb')
message.attach(MIMEImage(fp.read()))
fp.close()

session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')