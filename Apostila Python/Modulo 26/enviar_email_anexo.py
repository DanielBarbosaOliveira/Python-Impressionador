# Protocolo SMTP: Usado para envios de e-mail

import os
import smtplib
from senha_email import senha_app
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def enviar_email():
    msg = MIMEMultipart()
    msg["Subject"] = "Email enviado com Python"
    msg["From"] = "santos7mana@gmail.com"
    msg["To"] = "dan.dam@hotmail.com"
    msg["Cc"] = "santos7mana+copia@gmail.com"
    #msg["Bcc"] = "dan.dam@hotmail.com"
    
    link_imagem = "https://www.hashtagtreinamentos.com/wp-content/themes/hashtag/desenvolvimento_hashtag/assets/imgs/Global/logo-hashtag-224.webp"
    
    corpo_email = f"""<p>Boa tarde</p>
    <p>Testando outro e-mail com python usando smtplib</p>
    <p>Att., Daniel</p>
    <img src='{link_imagem}'>"""
    
    msg.attach(MIMEText(corpo_email, 'html'))
    
    # Anexar arquivos
    lista_arquivos = os.listdir('anexos')
    for nome_arquivo in lista_arquivos:
        with open(f'anexos/{nome_arquivo}', 'rb') as arquivo:
            msg.attach(MIMEApplication(arquivo.read(), Name=nome_arquivo))

    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(msg["From"], senha_app)
    servidor.send_message(msg)
    print('Email enviado')
    
enviar_email()