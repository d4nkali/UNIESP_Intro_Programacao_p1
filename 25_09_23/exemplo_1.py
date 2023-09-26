# Exemplo lista 4 questão 8
# Sistemas Para Internet - p1 b
# Aluno: Danilo Pereira Viana

h_extras = int(input('Digite a quantidade de horas extras: '))

h_faltou = int(input('Digite a quantidade de horas que faltou: '))

if h_extras > h_faltou + (h_faltou/2):
    print('Bônus de R$ 500.00')

else:
    print('Sem bônus')