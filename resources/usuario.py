from flask_restful import Resource, reqparse
from models.usuario import UsuarioModel

usuarios = [
    {
    'nome': 'Ana',
    'sobrenome': 'Botelho',
    'cpf': 123456,
    'email': 'ana@gmail.com',
    'nascimento': '16/12/1997',
    'id': 1
    },
{
    'nome': 'Luiza',
    'sobrenome': 'Primo',
    'cpf': 789123,
    'email': 'luiza@gmail.com',
    'nascimento': '16/12/1997',
    'id': 2
    }
]
#lista usuarios
class Usuarios(Resource):
    def get(self):
        return {'usuarios': usuarios}


class Usuario(Resource):
    #argumentos passados para os dados do usuario
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('sobrenome')
    argumentos.add_argument('cpf')


    #verifica se o usuraio ja existe
    def find_usuario(nome):
        for usuario in usuarios:
            if usuario['nome'] == nome:
                return usuario
    #retorna usuario pelo nome
    def get(self, nome):
        usuario = Usuario.find_usuario(nome)
        if usuario:
            return usuario
        return {'message': "Usuario nao encontrado"}, 404 #not found
    #cria novo usuario
    def post(self, nome):
        dados = Usuario.argumentos.parse_args()
        usuario_objeto = UsuarioModel(nome, **dados)
        novo_usuario = usuario_objeto.json()
        usuarios.append(novo_usuario)
        return novo_usuario, 200

    #editar usuario ou criar novo
    def put(self, nome):
        dados = Usuario.argumentos.parse_args()
        usuario_objeto = UsuarioModel(nome, **dados)
        novo_usuario = usuario_objeto.json()
        usuario = Usuario.find_usuario(nome)
        if usuario:
            usuario.update(novo_usuario)
            return novo_usuario, 200 #OK
        usuarios.append(novo_usuario)
        return novo_usuario, 201 #created


    def delete(self, nome):
        global usuarios
        usuarios = [usuario for usuario in usuarios if usuario['nome'] != nome]
        return {'message': 'Usuario deletado'}