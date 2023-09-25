h_extras = int(input('Digite a quantidade de horas extras: '))

h_faltou = int(input('Digite a quantidade de horas que faltou: '))

if h_extras > h_faltou:
    print('Bônus de R$ 500.00')

else:
    print('Sem bônus')