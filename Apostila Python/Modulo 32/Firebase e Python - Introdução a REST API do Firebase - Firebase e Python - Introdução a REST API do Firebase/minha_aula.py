# Criar o projeto no Firebase

# Link documento REST API Firebase
# https://firebase.google.com/docs/reference/rest/database

# Criar o Database (atenção às regras de segurança)
# Estrutura de árvore

# Interação com o Database (REST API)

import requests
import json

link = "https://meuprojetodaniel-700ee-default-rtdb.firebaseio.com/"

# Criar uma venda (POST)
# dados = {"cliente": "Felipe", "preco": 150, "produto": "teclado"}
# requisicao = requests.post(f"{link}/Vendas/.json",data=json.dumps(dados))
# print(requisicao)
# print(requisicao.text)

# Criar um novo produto (POST)
# dados = {"nome": "teclado", "preco": 150, "quantidade": 80}
# requisicao = requests.post(f"{link}/Produtos/.json",data=json.dumps(dados))
# print(requisicao)
# print(requisicao.text)

# Editar a venda (PATCH)
# dados = {"cliente": "Daniel"}
# requisicao = requests.patch(f"{link}/Vendas/-OzIAX3Vjo-UGLf3Y3zc/.json",data=json.dumps(dados))
# print(requisicao)
# print(requisicao.text)

# Pegar uma venda específico ou todas as vendas (GET)
requisicao = requests.get(f"{link}/Vendas/.json")
print(requisicao)
dic_requisicao = requisicao.json()
id_felipe = None
for id_venda in dic_requisicao:
    cliente = dic_requisicao[id_venda]["cliente"]
    if cliente == "Felipe":
        print(id_venda)
        id_felipe = id_venda
        
# Deletar uma venda (DELETE)
requisicao = requests.delete(f"{link}/Vendas/{id_felipe}/.json")
print(requisicao)
print(requisicao.text)