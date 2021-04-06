from flask import Flask
from flask_restful import Api
from resources.usuario import Usuarios, Usuario
import os
import psycopg2


app = Flask(__name__)
DATABASE_URL = 'postgres://brpshlcleineao:b301982db457e10bba8280a75a41225e061561e5280d3674d1d96fe53f5bfc37@ec2-54-205-183-19.compute-1.amazonaws.com:5432/dago63f5ao2noh'
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://brpshlcleineao:b301982db457e10bba8280a75a41225e061561e5280d3674d1d96fe53f5bfc37@ec2-54-205-183-19.compute-1.amazonaws.com:5432/dago63f5ao2noh'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.route('/')
def index():
    return '<h1>Teste<h1/>'

@app.before_first_request
def cria_banco():
    banco.create_all()

api.add_resource(Usuarios, '/users')
api.add_resource(Usuario, '/users/<int:cpf>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)

