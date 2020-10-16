from flask_restful import Resource, reqparse
from models.usuario import UsuarioModel

usuarios = [
    {
    'cpf': 123456,
    'nome': 'Ana',
    'sobrenome': 'Botelho',
    'email': 'ana@gmail.com',
    'nascimento': '16/12/1997',
    'id': 1
    },
{
    'cpf': 789123,
    'nome': 'Luiza',
    'sobrenome': 'Primo',
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
    argumentos.add_argument('nome')
    argumentos.add_argument('sobrenome')
    argumentos.add_argument('email')
    argumentos.add_argument('nascimento')
    argumentos.add_argument('id')



    #verifica se o usuraio ja existe pelo cpf
    def find_usuario(cpf):
        for usuario in usuarios:
            if usuario['cpf'] == cpf:
                return usuario
    #retorna usuario pelo cpf
    def get(self, cpf):
        usuario = Usuario.find_usuario(cpf)
        if cpf:
            return usuario
        return {'message': "Usuario nao encontrado"}, 404 #not found
    #cria novo usuario pelo cpf
    def post(self, cpf):
        dados = Usuario.argumentos.parse_args()
        usuario_objeto = UsuarioModel(cpf, **dados)
        novo_usuario = usuario_objeto.json()
        usuarios.append(novo_usuario)
        return novo_usuario, 200

    #editar usuario ou criar novo pelo cpf
    def put(self, cpf):
        dados = Usuario.argumentos.parse_args()
        usuario_objeto = UsuarioModel(cpf, **dados)
        novo_usuario = usuario_objeto.json()
        usuario = Usuario.find_usuario(cpf)
        if cpf:
            usuario.update(novo_usuario)
            return novo_usuario, 200 #OK
        usuarios.append(novo_usuario)
        return novo_usuario, 201 #created

    #deletar usuario pelo cpf
    def delete(self, cpf):
        global usuarios
        usuarios = [usuario for usuario in usuarios if usuario['cpf'] != cpf]
        return {'message': 'Usuario deletado'}