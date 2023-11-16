from email.message import EmailMessage
import smtplib
import ssl

password = open('senha.txt', 'r').read()

from_email = 'arthursantos242568@gmail.com'
to_email = 'arthursantos242568@gmail.com'
subject = 'Proposta de Parceria'
body = open('files/corpo.txt', 'r', encoding='utf-8').read()

# 1 - Montando estrutura do email
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

message.set_content(body)
safe = ssl.create_default_context()

# 2 - Envio de email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe ) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )
    print('email enviado!')