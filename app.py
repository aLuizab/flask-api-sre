from flask import Flask
from flask_restful import Api
from resources.usuario import Usuarios, Usuario
import os
import psycopg2


app = Flask(__name__)
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://sligvgaxcuplpn:9e8446c8f5f25489a9b91f8566987ac7472fcb4b06bd2400e9d6575f965d46f2@ec2-35-174-127-63.compute-1.amazonaws.com:5432/d8mq86ue2m3lah'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.route('/')
def index():
    return '<h1>Teste<h1/>'

#@app.before_first_request
#def cria_banco():
   # banco.create_all()

api.add_resource(Usuarios, '/users')
api.add_resource(Usuario, '/users/<int:cpf>')

if __name__ == '__main__':
    #from sql_alchemy import banco
    #banco.init_app(app)
    app.run(debug=True)

