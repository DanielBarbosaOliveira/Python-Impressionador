from ContasBancos import ContaCorrente, CartaoCredito


conta_daniel = ContaCorrente('Daniel', '111.222.333-45', 1234, 34062)

cartao_daniel = CartaoCredito('Daniel', conta_daniel)

cartao_daniel.senha = '1982'
print(cartao_daniel.senha)

print(conta_daniel.__dict__)
print(cartao_daniel.__dict__)