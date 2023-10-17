from random import randint

num_clientes = 1000
list_resp = []

while num_clientes > 0:
    list_resp.append(randint(1, 5))
    num_clientes -= 1

nota_1 = list_resp.count(1)
nota_2 = list_resp.count(2)
nota_3 = list_resp.count(3)
nota_4 = list_resp.count(4)
nota_5 = list_resp.count(5)

print(f'Quantidade de 1: {nota_1}')
print(f'Quantidade de 2: {nota_2}')
print(f'Quantidade de 3: {nota_3}')
print(f'Quantidade de 4: {nota_4}')
print(f'Quantidade de 5: {nota_5}')