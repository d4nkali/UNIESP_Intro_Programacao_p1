with open ('06_11_23\\teste2.txt', 'w', encoding='utf-8') as file:
    file.write('Corsa\n')
    file.write('Uno\n')
    file.write('Kombi\n')
    file.write('Santana\n')

with open('06_11_23\\teste2.txt', 'a', encoding='utf-8') as carro:
    for i in range(3):
        meu_carro = input('Digite um novo carro: ')
        carro.write(meu_carro + '\n')