from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/personagens')
def personagens():
    lista = [
        {"nome": "Abigail", "desc": "Aventureira que ama mineração."},
        {"nome": "Sebastian", "desc": "Programador introvertido."},
        {"nome": "Penny", "desc": "Professora gentil."},
        {"nome": "Shane", "desc": "Trabalha no JojaMart."}
    ]
    return render_template('personagens.html', personagens=lista)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run(debug=True)