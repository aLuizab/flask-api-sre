from flask_restful import Resource, reqparse
from models.usuario import UsuarioModel

#lista usuarios
class Usuarios(Resource):
    def get(self):
        return {'usuarios': [usuario.json() for usuario in UsuarioModel.query.all()]}


class Usuario(Resource):
    #argumentos passados para os dados do usuario
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True)
    argumentos.add_argument('sobrenome', type=str, required=True)
    argumentos.add_argument('email')
    argumentos.add_argument('nascimento')

    #retorna usuario pelo cpf
    def get(self, cpf):
        usuario = UsuarioModel.find_usuario(cpf)
        if cpf:
            return usuario.json()
        return {'message': "Usuario nao encontrado."}, 404 #not found
    #cria novo usuario pelo cpf
    def post(self, cpf):
        #verifica se o usuario existe
        if UsuarioModel.find_usuario(cpf):
            return {"messege": "Usuario de CPF '{}' já existe.".format(cpf)}, 400 #Bad request
        #se nao existe, cria um novo usuario
        dados = Usuario.argumentos.parse_args()
        usuario = UsuarioModel(cpf, **dados)
        try:
            usuario.save_usuario()
        except:
            return {'message': 'Ocorreu um erro interno ao tentar salvar o usuario.'}, 500 #internal sever error
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
        try:
            usuario.save_usuario()
        except:
            return {'message': 'Ocorreu um erro interno ao tentar salvar o usuario.'}, 500  # internal sever error
        return usuario.json(), 201 #created

    #deletar usuario pelo cpf
    def delete(self, cpf):
        usuario = UsuarioModel.find_usuario(cpf)
        if usuario:
            try:
                usuario.delete_usuario()
            except:
                return {'message': 'Ocorreu um erro ao tentar deletar o usuario'}
            return {'message': 'Usuario deletado'}
        return {'message': 'Usuario não encontrado'}, 404

