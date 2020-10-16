from flask_restful import Resource, reqparse
from models.usuario import UsuarioModel

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

    #retorna usuario pelo cpf
    def get(self, cpf):
        usuario = UsuarioModel.find_usuario(cpf)
        if cpf:
            return usuario.json()
        return {'message': "Usuario nao encontrado"}, 404 #not found
    #cria novo usuario pelo cpf
    def post(self, cpf):
        #verifica se o usuario existe
        if UsuarioModel.find_usuario(cpf):
            return {"messege": "Usuario de CPF '{}' já existe.".format(cpf)}, 400 #Bad request
        #se nao existe, cria um novo usuario
        dados = Usuario.argumentos.parse_args()
        usuario = UsuarioModel(cpf, **dados)
        usuario.save_usuario()
        return usuario.json()

    #editar usuario ou criar novo pelo cpf
    def put(self, cpf):
        dados = Usuario.argumentos.parse_args()
        usuario_encontrado = UsuarioModel.find_usuario(cpf)
        if usuario_encontrado:
            usuario_encontrado.update_usuario(**dados)
            usuario_encontrado.save_usuario()
            return usuario_encontrado.json(), 200 #OK
        usuario = UsuarioModel(cpf, **dados)
        usuario.save_usuario()
        return usuario.json(), 201 #created

    #deletar usuario pelo cpf
    def delete(self, cpf):
        global usuarios
        usuarios = [usuario for usuario in usuarios if usuario['cpf'] != cpf]
        return {'message': 'Usuario deletado'}