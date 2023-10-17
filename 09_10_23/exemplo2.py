# Agenda

contatos = [
    ['policia', '190' ''],
    ['samu', '192', ''],
    ['mãe', '(83) 9 5555-5555'],
    ['bombeiros', '193', '']
]

print(contatos[0][1])

lista_samu = contatos[1]
print()

print(lista_samu[1])

print()

for contato in contatos:
    print(f'Nome: {contato[0]} | Telefone: {contato[1]}')

print()