# API

# - Requisições (requests, get, post, patch, delete)

# - Biblioteca (sendgrid)

chave_api_sendgrid = "sua_chave_api"

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

conta_sendgrid = SendGridAPIClient(chave_api_sendgrid)

email = Mail(from_email="seuremetente@gmail.com", to_emails='seu_destinatario@hotmail.com', 
             subject="Email enviado pelo Sendgrid no Python", 
             html_content="<p>Email enviado com sucesso, seja bem vindo</p><p>Abraços e até o próximo e-mail.</p>")

resposta = conta_sendgrid.send(email)
print(resposta.status_code)


