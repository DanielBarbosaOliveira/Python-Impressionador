# %% [markdown]
# # Diminuindo o tamanho do executável final - Ambiente Virtual
# 
# ### Objetivo
# 
# Para diminuir o tamanho do arquivo a ser distribuído no final, vamos criar um ambiente virtual para garantir que teremos apenas as bibliotecas importantes.
# 
# - Passo 1: Garantir que o código está funcionando
# - Passo 2: Criar o ambiente virtual
# - Passo 3: Executar o nosso código por dentro do ambiente virtual
# - Passo 4: Identificar erros e instalar bibliotecas que faltam, apenas as que o programa pede.
# - Passo 5: Instalar o pyinstaller e transformar em executável o programa Python

# %%
#rodar o código de um programa que fazemos durante o curso que funcione. Exemplo o do outlook de enviar email
from twilio.rest import Client

account_sid = 'SEU_ACCOUNT_SID'
token = 'Seu token'

client = Client(account_sid, token)

remetente = '+17372508034'
destino = '+5565999088840'

message = client.messages.create(
    to=destino, 
    from_=remetente,
    body="sms_appointment_reminders")

print(message.sid)


