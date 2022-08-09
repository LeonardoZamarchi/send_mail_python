import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
from email.mime.base import MIMEBase 
from email import encoders 
import os.path


def send_email(email_recipient,
               email_subject,
               email_message,
               attachment_location=''):

    email_sender = ''

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_recipient
    msg['Subject'] = email_subject

    msg.attach(MIMEText(email_message, 'plain'))

    if attachment_location != '':
        filename = os.path.basename(attachment_location)
        attachment = open(attachment_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        "attachment; filename= %s" % filename)
        msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.address', port)
        server.ehlo()
        server.starttls()
        server.login('mail', 'pwd')
        text = msg.as_string()
        server.sendmail(email_sender, email_recipient, text)
        print('email sent to ' + email_recipient)
        server.quit()
    except Exception as e:
        print("SMPT server connection error: ", str(e))
        print(e)
    return True 


send_email('to','subject','message','attachment')

