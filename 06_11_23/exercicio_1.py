# Exercicio 1 - Crie um programa Python que imprima todas as linhas deste aquivo;
# E conte quantas linhas tem neste aquivo.

with open('06_11_23\\Moby-Dick.txt', 'r', encoding='utf-8') as livro:
    ler = livro.read()
    print(ler)
    print()
    print()
    print('#####################################################')

with open('06_11_23\\Moby-Dick.txt', 'r', encoding='utf-8') as livro:
    linhas = livro.readlines()
    print(f'A quantidade de linhas é: {len(linhas)}')