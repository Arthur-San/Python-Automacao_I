from email.message import EmailMessage
import smtplib
import ssl
import mimetypes

password = open('senha.txt', 'r').read()

from_email = 'arthursantos242568@gmail.com'
to_email = 'arthursantos242568@gmail.com'
subject = 'Proposta de Parceria Customizada'
body = open('files/index.html.txt', 'r', encoding='utf-8').read()

# 1 - Montando estrutura do email
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

message.set_content(body, subtype="html")
safe = ssl.create_default_context()

# 2 - Adicionar anexo
