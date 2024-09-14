import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(email,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('mahimaplatinum41@gmail.com','lkkw ounh nfoa mltt')
    msg=EmailMessage()
    msg['FROM']='mahimaplatinum41@gmail.com'
    msg['TO']=email
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()