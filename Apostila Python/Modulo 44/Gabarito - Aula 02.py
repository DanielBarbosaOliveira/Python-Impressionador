import tkinter as tk

janela = tk.Tk()

janela.title("Cotação de Moedas")

mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas")
mensagem.pack()

mensagem2 = tk.Label(text="Selecione a moeda desejada")
mensagem2.pack()

janela.mainloop()

