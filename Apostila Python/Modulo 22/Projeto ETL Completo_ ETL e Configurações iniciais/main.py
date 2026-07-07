# 5 Funções essenciais do Pandas que todo programador Precisa saber
import pandas as pd


dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'],
    'Idade': [25, 30, 35, 40, 45],
    'Salário': [3000, None, 7000, None, 11000]
}
tabela = pd.DataFrame(dados)

# describe
#print(tabela.describe())

# apply
tabela['Salário_Ajustado'] = tabela['Salário'].apply(lambda x: x * 1.1)
#print(tabela)

# fillna
media_salario = tabela['Salário'].mean()
tabela['Salário'] = tabela['Salário'].fillna(media_salario)
tabela['Salário_Ajustado'] = tabela['Salário_Ajustado'].fillna(tabela['Salário_Ajustado'].mean())

print(tabela)

# merge

tabela_area = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'],
    'Área': ['Administrativo', 'Financeiro', 'Vendas', 'Administrativo', 'Financeiro']
})

tabela = tabela.merge(tabela_area, on='Nome', how='left')
print(tabela)

# groupby
medias_areas = tabela.groupby('Área').mean(numeric_only=True)
print(medias_areas)