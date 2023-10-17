# TED 9 - Introdução a programação - Sistemas para Internet p1 B
# Aluno: Danilo Pereira Viana

# Criando o glossário
glossario = {
    "Algoritmos": "Sequência de instruções que resolvem um problema.",
    "Lógica": "O uso correto das ordem da razão",
    "Variavel": "Um dado armazenado que possa mudar ao decorrer do tempo",
    "Python": "Uma linguagem de programação de alto nível e fácil de aprender.",
    "Visual Studio Code": "Uma IDE de diversas linguagens e gratuito."
}

# Listando o glossário 
for palavra, significado in glossario.items():
    print(f"{palavra}:\n{significado}\n")
