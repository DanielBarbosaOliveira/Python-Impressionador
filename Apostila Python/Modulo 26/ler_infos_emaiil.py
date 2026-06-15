# Protocolo IMAP = Pegar informações de e-mail
from senha_email import senha_app
from imap_tools import MailBox, AND

usuario = 'santos7mana@gmail.com'
senha = senha_app

meu_email = MailBox('imap.gmail.com').login(usuario, senha) # Após passar usuario e senha tem como passar uma pasta como parametro para setar ela: '[Gmail]/E-mails enviados'

# Ver pastas disponíveis no e-mail
""" for pasta in meu_email.folder.list():
    print(pasta) """

# meu_email.folder.set('Pasta escolhida') seta a pasta que deseja ver
 
lista_emails = meu_email.fetch(AND(from_='santos7mana@gmail.com', to='dan.dam@hotmail.com'))

for i, email in enumerate(lista_emails):
    if len(email.attachments) > 0:
        print(email.subject)
        print(email.text)
        print(email.html)
        for anexo in email.attachments:
            with open(f'Email {i+1} - {anexo.filename}', 'wb') as arquivo:
                arquivo.write(anexo.payload)
            print(f'Anexo: {anexo.filename}')
            