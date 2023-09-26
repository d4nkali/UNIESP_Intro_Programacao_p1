# Exemplo lista 4 questão 7
# Sistemas Para Internet - p1 b
# Aluno: Danilo Pereira Viana

valor = int(input('Digite o valor da comprar: '))

if valor >= 100:
    compras = (valor * 10/100)
    print(f'O valor {valor} está com 10% off; total pago de {valor - compras}')

elif valor >= 50 < 100:
    compras = (valor * 5 /100)
    print(f'O valor {valor} está com 5% off; total pago de {valor - compras}')

elif valor < 50:
    compras = valor
    print(f'O valor {valor} está sem desconto; total pago de {valor}')

else:
    print('Erro')