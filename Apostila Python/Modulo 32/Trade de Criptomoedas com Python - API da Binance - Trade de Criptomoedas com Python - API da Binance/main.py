from binance.client import Client
from chaves_binance import API_KEY, SECRET_KEY

client = Client(API_KEY, SECRET_KEY)

# pegar informações da conta
info = client.get_account()
for item in info:
    print(item)
    
# ver os saldos dos ativos que temos na conta
lista_ativos = info["balances"]

for ativo in lista_ativos:
    if float(ativo["free"]) > 0:
        print(ativo)

# criar uma ordem dentro da binance
# from binance.enums import *
# order = client.create_order(
#     symbol="BNBBRL",
#     side=SIDE_BUY, # ou SIDE_SELL
#     type=ORDER_TYPE_MARKET, # ou ORDER_TYPE_LIMIT
#     #time_in_force=TIME_IN_FORCE_GTC,
#     quantity=0.01,
#     #price="0.0001"
# )
# print(order)

# visualizar as ordens executadas
print(client.get_all_orders(symbol="BNBBRL"))
print(client.get_my_trades(symbol="BNBBRL"))

# te mostrar as referencias de cada par de moedas
print(client.get_symbol_info("BNBBRL"))

# pegar as cotacoes em tempo real
transacoes = client.get_recent_trades(symbol="BNBBRL", limit=1)
print(transacoes)