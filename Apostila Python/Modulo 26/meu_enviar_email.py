import smtplib
from senha_email import senha_app
from email.message import EmailMessage


def enviar_email():
    msg = EmailMessage()

    msg["Subject"] = "Mais um teste"
    msg["From"] = "santos7mana@gmail.com"
    msg["To"] = "dan.dam@hotmail.com"

    corpo_email = """<p>Boa tarde</p>
    <p>Este é meu primeiro e-mail com python usando smtplib</p>
    <p>Att., Daniel</p>"""
    
    msg.set_content(corpo_email, subtype="html")

    with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
        servidor.starttls()
        servidor.login(msg["From"], senha_app)
        servidor.send_message(msg)

    print('Email enviado')

enviar_email()