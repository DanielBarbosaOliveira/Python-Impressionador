import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

def abrir_calendario(campo_alvo):
    janela_calendario = tk.Toplevel(janela)
    janela_calendario.title('Selecionar Data')

    calendario = Calendar(janela_calendario, selectmode='day', year=2026)
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
    pass

def selecionar_arquivo():
    pass

janela = tk.Tk()
janela.title('Ferramenta de Cotacão de Moedas')

estilo = ttk.Style()
estilo.theme_use('clam')

lista_moedas = ['USD', 'EUR']

label_cotacaomoeda = tk.Label(text='Cotação de 1 Moeda Específica', borderwidth=2, relief='solid')
label_cotacaomoeda.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_selecionarmoeda = tk.Label(text='Selecionar Moeda', anchor='e')
label_selecionarmoeda.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionarmoeda = ttk.Combobox(values=lista_moedas)
combobox_selecionarmoeda.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

label_selecionardia = tk.Label(text='Selecione o dia que deseja pegar a cotação', anchor='e')
label_selecionardia.grid(row=2, column=0, padx=10, pady=10, sticky='nswe')

data_moeda = tk.Entry(janela, state='readonly', justify='center')
data_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

calendario_moeda = tk.Button(janela, text="Escolher Data 📅", command=lambda: abrir_calendario(data_moeda))
calendario_moeda.grid(row=2, column=1, padx=10, pady=10, sticky='nswe')

label_textocotacao = tk.Label(text='')
label_textocotacao.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

botao_pegarcotacao = tk.Button(text='Pegar cotação', command=pegar_cotacao)
botao_pegarcotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

# Cotação de várias moedas

label_cotacaovariasmoedas = tk.Label(text='Cotação de Múltiplas Moedas', borderwidth=2, relief='solid')
label_cotacaovariasmoedas.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_selecionararquivo = tk.Label(text='Selecione um Arquivo em Excel com as Moedas na Coluna A')
label_selecionararquivo.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

botao_selecionararquivo = tk.Button(text='Clique para Selecionar:', command=selecionar_arquivo)
botao_selecionararquivo.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

label_arquivoselecionado = tk.Label(text='Nenhum Arquivo Selecionado', anchor='e')
label_arquivoselecionado.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_datainicial = tk.Label(text='Data Inicial')
label_datafinal = tk.Label(text='Data Final')
label_datainicial.grid(row=7, column=0, padx=10, pady=10, sticky='nswe')
label_datafinal.grid(row=8, column=0, padx=10, pady=10, sticky='nswe')

calendario_moeda = tk.Button(janela, text="Escolher Data 📅", command=abrir_calendario)
calendario_moeda.grid(row=2, column=1, padx=10, pady=10, sticky='nswe')

entry_data = tk.Entry(janela, state='readonly', justify='center')
entry_data.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

calendario_datainicial = tk.Button(janela, text="Escolher Data 📅", command=abrir_calendario)
calendario_datafinal = tk.Button(janela, text="Escolher Data 📅", command=abrir_calendario)
calendario_datainicial.grid(row=7, column=1, padx=10, pady=10, sticky='nswe')
calendario_datafinal.grid(row=8, column=1, padx=10, pady=10, sticky='nswe')

entry_data = tk.Entry(janela, state='readonly', justify='center')
entry_data.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

janela.mainloop()
