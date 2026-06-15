# Protocolo SMTP: Usado para envios de e-mail

import smtplib
import email.message
from senha_email import senha_app

def enviar_email():
    msg = email.message.Message()
    msg["Subject"] = "Email enviado com Python"
    msg["From"] = "santos7mana@gmail.com"
    msg["To"] = "dan.dam@hotmail.com, albertobalboa22@gmail.com"
    msg["Cc"] = "santos7mana@gmail.com"
    #msg["Bcc"] = "dan.dam@hotmail.com"
    
    link_imagem = "https://www.hashtagtreinamentos.com/wp-content/themes/hashtag/desenvolvimento_hashtag/assets/imgs/Global/logo-hashtag-224.webp"
    
    corpo_email = f"""<p>Bom dia, Caro Sr. Alberto.</p>
    <p>Este é um e-mail enviado com python através do protocolo SMTP</p>
    <p>Para um auxilio no meu desenvolvimento e talvez algum auxilio para ti, envie-me alguns conjuntos de dados e me peça para responder algumas perguntas com os dados.</p>
    <p>Caso deseje algum exemplo de conjuntos de dados, o <a href="https://www.kaggle.com/datasets">Kaggle</a> possui vários conjuntos de dados interessantes disponibilizados por empresas: .</p>
    <p>Att., Daniel</p>
    """
    #<img src='{link_imagem}'>
    
    corpo_email = corpo_email.encode('latin1')
    
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(msg["From"], senha_app)
    servidor.send_message(msg)
    print('Email enviado')
    
enviar_email()