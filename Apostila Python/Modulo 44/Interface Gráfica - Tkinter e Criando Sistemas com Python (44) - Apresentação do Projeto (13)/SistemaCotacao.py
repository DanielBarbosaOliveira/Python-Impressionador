import requests
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkcalendar import Calendar
from tkinter.filedialog import askopenfilename


def abrir_calendario(campo_alvo):
    janela_calendario = tk.Toplevel(janela)
    janela_calendario.title('Selecionar Data')

    calendario = Calendar(janela_calendario, selectmode='day', year=2026, date_pattern='dd/mm/yyyy')
    calendario.pack(padx=10, pady=10)

    def selecionar_data():
        data_formatada = calendario.get_date()

        campo_alvo.config(state='normal')
        campo_alvo.delete(0, tk.END)
        campo_alvo.insert(0, data_formatada)
        campo_alvo.config(state='readonly')

        janela_calendario.destroy()

    btn_confirmar = tk.Button(janela_calendario, text='Confirmar', command=selecionar_data)
    btn_confirmar.pack(pady=5)


def pegar_cotacao():
    moeda = combobox_selecionarmoeda.get()
    data_cotacao = entry_data_moeda.get()
    dia, mes, ano = data_cotacao.split('/')
    link = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}'
    requisicao_moeda = requests.get(link)
    cotacao = requisicao_moeda.json()
    valor_moeda = cotacao[0]['bid']
    label_textocotacao['text'] = f"A cotação de {moeda} no dia {dia}/{mes}/{ano} foi de : R$ {float(valor_moeda):,.2f}"


def selecionar_arquivo():
    caminho_arquivo = askopenfilename(title='selecione o Arquivo de Moeda')
    var_caminhoarquivo.set(caminho_arquivo)
    if caminho_arquivo:
        label_arquivoselecionado['text'] = f'Arquivo selecionado: {caminho_arquivo}'

def atualizar_cotacoes():
    try:
        df = pd.read_excel(var_caminhoarquivo.get())
        moedas = df.iloc[:, 0]
        data_inicial = entry_datainicial.get()
        data_final = entry_datafinal.get()
        dia_inicial, mes_inicial, ano_inicial = data_inicial.split('/')
        dia_final, mes_final, ano_final = data_final.split('/')

        for moeda in moedas:
            link = (f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/1000?'
                    f'start_date={ano_inicial}{mes_inicial}{dia_inicial}&'
                    f'end_date={ano_final}{mes_final}{dia_final}')

            requisicao_moeda = requests.get(link)
            cotacoes = requisicao_moeda.json()

            for cotacao in cotacoes:
                timestamp = int(cotacao['timestamp'])
                bid = float(cotacao['bid'])
                objeto_data = datetime.fromtimestamp(timestamp)
                data = datetime.strftime(objeto_data, '%d/%m/%y')
                if data not in df:
                    df[data] = np.nan

                df.loc[df.iloc[:, 0] == moeda,data] = bid

        df.to_excel('teste.xlsx')
        label_atualizarcotacoes['text'] = 'Arquivo Atualizado com Sucesso'

    except:
        label_atualizarcotacoes['text'] = 'Selecione um arquivo Excel no Formato Correto'

janela = tk.Tk()
janela.title('Ferramenta de Cotacão de Moedas')
# janela.config(bg='#F2EFE9')
# janela.option_add('*Background', '#F2EFE9')

lista_moedas = []
estilo = ttk.Style()
estilo.theme_use('clam')

url_awesomeapi = r'https://economia.awesomeapi.com.br/json/all'
requisicao = requests.get(url_awesomeapi)
dicionario_moedas = requisicao.json()

lista_moedas = list(dicionario_moedas.keys())

label_cotacaomoeda = tk.Label(text='Cotação de 1 Moeda Específica', borderwidth=2, relief='solid')
label_cotacaomoeda.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_selecionarmoeda = tk.Label(text='Selecionar Moeda', anchor='e')
label_selecionarmoeda.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionarmoeda = ttk.Combobox(values=lista_moedas)
combobox_selecionarmoeda.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

label_selecionardia = tk.Label(text='Selecione o dia que deseja pegar a cotação', anchor='e')
label_selecionardia.grid(row=2, column=0, padx=10, pady=10, sticky='nswe')

entry_data_moeda = tk.Entry(janela, state='readonly', justify='center')
entry_data_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

botao_data_moeda = tk.Button(janela, text="Escolher Data 📅", command=lambda: abrir_calendario(entry_data_moeda))
botao_data_moeda.grid(row=2, column=1, padx=10, pady=10, sticky='nswe')

label_textocotacao = tk.Label(text='')
label_textocotacao.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

botao_pegarcotacao = tk.Button(text='Pegar cotação', command=pegar_cotacao)
botao_pegarcotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

# Cotação de várias moedas

label_cotacaovariasmoedas = tk.Label(text='Cotação de Múltiplas Moedas', borderwidth=2, relief='solid')
label_cotacaovariasmoedas.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_selecionararquivo = tk.Label(text='Selecione um Arquivo em Excel com as Moedas na Coluna A')
label_selecionararquivo.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

var_caminhoarquivo = tk.StringVar()

botao_selecionararquivo = tk.Button(text='Clique para Selecionar:', command=selecionar_arquivo)
botao_selecionararquivo.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

label_arquivoselecionado = tk.Label(text='Nenhum Arquivo Selecionado', anchor='e')
label_arquivoselecionado.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_datainicial = tk.Label(text='Data Inicial', anchor='e')
label_datafinal = tk.Label(text='Data Final', anchor='e')
label_datainicial.grid(row=7, column=0, padx=10, pady=10, sticky='nswe')
label_datafinal.grid(row=8, column=0, padx=10, pady=10, sticky='nswe')

entry_datainicial = tk.Entry(janela, state='readonly', justify='center')
entry_datainicial.grid(row=7, column=2, padx=10, pady=10, sticky='nswe')

entry_datafinal = tk.Entry(janela, state='readonly', justify='center')
entry_datafinal.grid(row=8, column=2, padx=10, pady=10, sticky='nswe')

botao_datainicial = tk.Button(janela, text="Escolher Data 📅", command=lambda: abrir_calendario(entry_datainicial))
botao_datafinal = tk.Button(janela, text="Escolher Data 📅", command=lambda: abrir_calendario(entry_datafinal))
botao_datainicial.grid(row=7, column=1, padx=10, pady=10, sticky='nswe')
botao_datafinal.grid(row=8, column=1, padx=10, pady=10, sticky='nswe')

botao_atualizarcotacoes = tk.Button(text='Atualizar Cotacões', command=atualizar_cotacoes)
botao_atualizarcotacoes.grid(row=9, column=0, padx=10, pady=10, sticky='nswe')

label_atualizarcotacoes = tk.Label(text='')
label_atualizarcotacoes.grid(row=9, column=1, padx=10, pady=10, sticky='nswe', columnspan=2)

botao_fechar = tk.Button(text='Fechar', command=janela.quit)
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
