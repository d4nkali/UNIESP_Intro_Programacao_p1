# Exercicio 2 - Dado uma lista de números, crie um algoritmo que retorne a soma dos números 
# pares na lista. Exemplo de entrada: [1, 2, 3, 4, 5, 6]; Saída esperada: 12

from random import randint

res_soma = 0
lista = []

for n in range(5):
    lista.append(randint(1, 50))

for i in lista:
    if (i % 2) == 0:
        res_soma += i

print(f'O resultado da soma é: {res_soma}')
print()
print(lista)