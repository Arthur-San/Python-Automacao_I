from email.message import EmailMessage
import smtplib
import ssl

password = open('senha.txt', 'r').read()

from_email = 'arthursantos242568@gmail.com'
to_email = 'fernanda.foppa.2002@gmail.com'
subject = 'Curso Python'
body = """
Python pythando no python pythoso
"""

# 1 - estruturando a mensagem via email
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email

message.set_content(body)
safe = ssl.create_default_context()

# 2 - envio de email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(from_email, to_email, message.as_string())
