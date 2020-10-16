class UsuarioModel:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def json(self):
        return {
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'cpf': self.cpf
        }