# Dicionario

filmes = {
    1: ['Outono em NY', 'Romance', 789, 120],
    2: ['Exorcista', 'Terror', 456, 130],
    3: ['Ilha do medo', 'Suspense', 123, 120],
}

for indice in filmes:
    print(f'filme: {filmes[indice][0]}')
    print(f'genero: {filmes[indice][1]}')
    print(f'Duração: {filmes[indice][3]}')
    print(f'---------')