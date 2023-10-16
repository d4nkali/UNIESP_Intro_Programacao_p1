# Aluno: Danilo Pereira Viana / Sistemas da Internet p1B

# 2) Problema: As maçãs custam R$ 1,30 cada, se forem compradas menos de uma dúzia, e R$ 1,00 
# se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, 
# calcule e escreva o custo total da compra.

# Pergunta ao usuário o número de maçãs que comprou
numero_maca = int(input("Quantas maçãs você comprou? "))

# Definir o preço por maçã
preco_maca = 1.00  # Preço se comprar menos de 12

if numero_maca < 12: # Verificar se a quantidade é menor do que 12
    preco_maca = 1.30  # Preço se comprar mais que 12

# Calcular o custo total
custo_total = numero_maca * preco_maca

# Exibir o custo total 
print(f"O total foi de {custo_total:} R$")