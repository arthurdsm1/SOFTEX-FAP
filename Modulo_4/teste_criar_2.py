from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/clientes')
def clientes():
    clientes_lista = [
        {"id": 1, "nome": "João"},
        {"id": 2, "nome": "Maria"},
        {"id": 3, "nome": "Carlos"}
    ]
    return jsonify(clientes_lista)

if __name__ == '__main__':
    app.run(debug=True)
