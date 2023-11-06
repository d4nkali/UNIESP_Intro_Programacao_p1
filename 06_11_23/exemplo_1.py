# Leitura inteira

with open('06_11_23\\teste.txt', 'r', encoding='utf-8') as file_object:
    conteudo = file_object.read()
    print(conteudo)

print()
print('###################################################')
print()

# Leitura por linha de um txt

with open('06_11_23\\teste.txt', 'r', encoding='utf-8') as file_object:
    for linha in file_object:
        print(linha)

print()
print('###################################################')
print()

# Leitura por linha de um txt, limpando espaço em branco

with open('06_11_23\\teste.txt', 'r', encoding='utf-8') as file_object:
    for linha in file_object:
        print(linha.rsplit())

print()
print('###################################################')
print()