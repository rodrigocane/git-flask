from flask import Flask, render_template
from pessoa import *

app = Flask(__name__)

def cartao_pessoa(rota_pessoa):
    pessoa = pessoas.get(rota_pessoa)
    if not pessoa:
        return "Tá perdido, amigão?<BR><BR><a href='/' class=>← Voltar</a>", 404 
    return render_template("cartao.html", pessoa = pessoa)

@app.route("/cane")
def cane():
    '''Rota específica para o Cane. Você pode criar a sua se não quiser seguir o template'''
    return cartao_pessoa("cane")

@app.route("/<pessoa>")
def perfil(pessoa):
    '''Rota genérica para exibir o perfil de cada pessoa no formato padrão'''       
    return cartao_pessoa(pessoa)

@app.route("/")
def index():
    return render_template("index.html", pessoas=pessoas)

if __name__ == "__main__":
    app.run(port=5506, debug=True)