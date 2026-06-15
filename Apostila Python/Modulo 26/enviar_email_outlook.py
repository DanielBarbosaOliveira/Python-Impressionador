import win32com.client as win32
import os

outlook = win32.Dispatch('outlook.application')

email = outlook.CreateItem(0)

email.To = "santos7mana@gmail.com"
email.Cc = 'dan.dam@hotmail.com'
#email.Bcc = cópia oculta
email.Subject = "Email enviado pelo Outlook"

link_imagem = "https://www.hashtagtreinamentos.com/wp-content/themes/hashtag/desenvolvimento_hashtag/assets/imgs/Global/logo-hashtag-224.webp"
# email.Body = "Texto do e-mail"
email.HTMLBody = f"""<p>Meu primeiro paragrafo</p>
<p>Meu segundo paragrafo no email</p>
<img src='{link_imagem}' width=200>"""

caminho_codigo = os.getcwd()
lista_arquivos = os.listdir('anexos')
for nome_arquivo in lista_arquivos:
    caminho_anexo = os.path.join(caminho_codigo, 'anexos', nome_arquivo)
    email.Attachments.Add(caminho_anexo)

email.Send()