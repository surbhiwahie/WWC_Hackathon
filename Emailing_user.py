from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import smtplib, ssl

send_from = 'donationsecondchance@gmail.com'
send_to = ['surbhiwahie@gmail.com','jenailalesbianrobotics@gmail.com', 'akanksha.bhattachan@gmail.com']
title = ''
url = ''
subject = 'TEST email: Hello from second chance'  ## whatever subjectline you need to send
message_contents = """ 
<html>
    <body>
        <p><font color = "#404041">
        Hi,
        <br>
        <br>
        We are from Second chance. 
        <br>
        This is a test email.
        <br>
        <font face = "monospace">
        <br>
        <br>
        Thanks,
        <br>
        Second Chance
        </font></font></p>
    </body>
</html>
    """
server = 'smtp.gmail.com'
port = 587
username = 'donationsecondchance@gmail.com' ## this will change if we are creating a new emailID
password = '16 digit password' ## we will get this after 2 factor authentication
isTls = True
msg = MIMEMultipart()
msg['From'] = send_from
msg['To'] = ','.join(send_to)
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = subject
msg.attach(MIMEText(message_contents, "html"))
smtp = smtplib.SMTP(server, port)
if isTls:
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()