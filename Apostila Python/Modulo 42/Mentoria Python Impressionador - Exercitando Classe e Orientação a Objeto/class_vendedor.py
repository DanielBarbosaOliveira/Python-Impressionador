class Vendedor:

    def __init__(self, nome_vendedor):
        self.vendas = 0
        self.nome = nome_vendedor
        self.meta = 500
        self.bonus = 0

    def vendeu(self, quantidade_vendas):
        self.vendas = quantidade_vendas
        self.calcular_bonus()

    def calcular_bonus(self):
        if self.vendas > self.meta:
            self.bonus = 30
        else:
            self.bonus = 0