# Função global

variavel_global = "Global!!!"

def minha_funcao():
    print(variavel_global)

minha_funcao() # Imprime "Global!"

# Função Local

def funcao():
    local = 'Local!!!!'
    print(local)

funcao() # Imprime 'Local!!!