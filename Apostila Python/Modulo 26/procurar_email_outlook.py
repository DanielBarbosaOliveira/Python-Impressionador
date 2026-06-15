import win32com.client as win32
import os

outlook = win32.Dispatch('outlook.application')

caixas_email = outlook.GetNamespace('MAPI')

""" for pasta in caixas_email.Folders: # Mostra as pastas (contas) que tem dentro do outlook
    print(pasta) """
    
pasta_dandam = caixas_email.Folders.Item(1) # Escolhe a conta desejada, começando pelo numero 1

""" for subpastas in pasta_dandam.Folders: # Mostra as subpastas dentro da conta
    print(subpastas) """
    
caixa_entrada = pasta_dandam.Folders.Item(2)

lista_emails = caixa_entrada.Items
print(len(lista_emails))

for email in lista_emails:
    anexos = email.Attachments
    if email.To == 'santos7mana@hotmail.com' and len(anexos) > 0:
        print('-' * 20)
        print(email.Subject)
        print(email.Cc)
        print(email.Body)
        for anexo in anexos:
            print(anexo.FileName)
            caminho_codigo = os.getcwd()
            caminho_anexo_salvar = os.path.join(caminho_codigo, f"Email {email.Subject} - {anexo.FileName}")
            anexo.SaveAsFile(caminho_anexo_salvar)
        print('-' * 20)
print('Fim do código')
    