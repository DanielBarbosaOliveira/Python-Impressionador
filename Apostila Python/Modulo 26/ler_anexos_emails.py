from imap_tools import MailBox, AND

usuario = "seuemail@gmail.com"
senha = "sua_senha_app_aqui"

meu_email = MailBox("imap.gmail.com").login(usuario, senha)

# ver as pastas do meu email disponíveis
# for pasta in meu_email.folder.list():
#     print(pasta)

# meu_email.folder.set('[Gmail]/E-mails enviados')

lista_emails = meu_email.fetch(AND(from_="emailremetente@gmail.com", to="emaildestinatario@hotmail.com"))

for i, email in enumerate(lista_emails):
    if len(email.attachments) > 0:
        print(email.subject)
        print(email.text)
        print(email.html)
        for anexo in email.attachments:
            with open(f"Email {i+1} - {anexo.filename}", "wb") as arquivo:
                arquivo.write(anexo.payload)
            print("Anexo:", anexo.filename)
