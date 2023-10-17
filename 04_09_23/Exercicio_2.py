# Exercicio 2

# Cria as variaveis, espera a resposta do terminal e ler as 2 notas 
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a media aritimetica das 2 medias
media = (nota1 + nota2) / 2

if 10 > media >= 6:                     # Se a nota for maior que 6, então:
    print(f"Aluno aprovado com a media: {media}")    # imprime aprovado

elif 0 <= media < 6:                    # se for abaixo de 6
    print(f"Aluno reprovado com a media: {media}")

else:
    print(f"Valor errado -> {media}")