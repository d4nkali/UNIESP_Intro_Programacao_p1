from flask import Flask, render_template # Importa o flask

app = Flask(__name__) # Inicia o Flask dentro da variável app

@app.route('/')
# Cria a função oi e executa uma frase ou site html
def oi(): 
    #return '<h1>Olá, Mundo!</h1>'
    return render_template('modelo.html')

app.run() # Executa o servidor