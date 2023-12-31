import os
from flask import Flask, render_template # Importa o flask

app = Flask(__name__) # Inicia o Flask dentro da variável app

# Define a variavel de controle de ambiente
os.environ['FLASK_DEBUG'] = 'True'

# Configurar o debug
app.debug = os.environ.get('FLASK_DEBUG') == "True"

@app.route('/')
# Cria a função oi e executa uma frase ou site html
def oi(): 
    #return '<h1>Olá, Mundo!</h1>'
    return render_template('index.html')

if __name__ == "__main__":
    app.run() # Executa o servidor