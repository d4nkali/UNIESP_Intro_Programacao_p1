# Exercicio 1

from random import randint

Q = []

for numero in range(20):
    Q.append(randint(1, 100))

# Variavel de controle
maior = -1
menor = 101

for i in Q:
    if maior < i:
        maior = i
    
    if menor > i:
        menor = i

print(Q)
print()
print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')
print()
print(max(Q))
print(min(Q))