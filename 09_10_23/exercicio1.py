# Criar uma lista com 5 clubes

clubes_de_futebol = [
    'ibis',
    'flamengo',
    'perilima',
    'volta redonda',
    'nacional de patos',
]

# Perguntar qual o clube o usuario vai verificar
clube_pesq = input('Digite o clube: ')

for clube in clubes_de_futebol:
    if clube == clube_pesq:
        print('Achei')

    else:
        print('Não Encontrado')