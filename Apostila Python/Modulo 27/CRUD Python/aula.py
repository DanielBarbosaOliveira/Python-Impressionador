import mysql.connector
from senhas import senha_mysql

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password=senha_mysql,
    database='bd_youtube'
)

cursor = conexao.cursor()
# CRUD
nome_produto = "Todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()


cursor.close()
conexao.close()


# Create
""" nome_produto = 'Chocolate'
valor = 15
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() """

# Read
""" comando = 'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado) """

# Update
""" valor = 6
nome_produto = "Todynho"
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() """