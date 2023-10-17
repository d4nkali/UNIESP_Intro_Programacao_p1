# Exemplo random
# Sistemas Para Internet - p1 b
# Aluno: Danilo Pereira Viana

from random import randint

print('Os numeros sorteados foram: ')
print()

for d100 in range(10):
    resultado = randint(1, 100)
    print(resultado)

print()