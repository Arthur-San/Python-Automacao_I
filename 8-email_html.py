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

anexo = 'files/corpo.txt'
# print(mimetypes.guess_type(anexo)[0])
mimetype, mimesubtype = mimetypes.guess_type(anexo)[0].split('/')
with open(anexo, 'rb') as a:
    message.add_attachment(
        a.read(),
        maintype=mimetype,
        subtype=mimetype,
        filename=anexo
    )
    
# 3 - Envio de email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe ) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )
    print('email enviado!')
    