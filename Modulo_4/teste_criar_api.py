from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.db'
db = SQLAlchemy(app)

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)

@app.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    clientes_lista = [{"id": c.id, "nome": c.nome} for c in clientes]
    return jsonify(clientes_lista)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
