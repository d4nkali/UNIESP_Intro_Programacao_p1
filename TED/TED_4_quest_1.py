# Aluno: Danilo Pereira Viana / Sistemas da Internet p1B

# 1) Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou 
# negativo (considere o valor zero como positivo).

# Manda o usuario digitar o numero
numero = float(input("Digite o numero: "))

# Verificar se o numero é positivo ou negativo (considerando zero como positivo)
if numero >= 0: # Se for maior ou igual a zero
    print("O numero é positivo.")
else: # Se menor
    print("O numero é negativo.")