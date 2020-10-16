from sql_alchemy import banco


class UsuarioModel(banco.Model):
    __tablename__ = 'usuarios'

    cpf = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(80))
    sobrenome = banco.Column(banco.String(80))
    email = banco.Column(banco.String(80))
    nascimento = banco.Column(banco.Integer)


    def __init__(self, cpf, nome, sobrenome, email, nascimento):
        self.cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self. nascimento = nascimento

    def json(self):
        return {
            'cpf':self.cpf,
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'email': self.email,
            'nascimento': self.nascimento,
        }

    @classmethod
    def find_usuario(cls, cpf):
        usuario = cls.query.filter_by(cpf=cpf).first()
        if usuario:
            return usuario
        return None

    def save_usuario(self):
        banco.session.add(self)
        banco.session.commit()

    def update_usuario(self, nome, sobrenome, email, nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.nascimento = nascimento

    def delete_usuario(self):
        banco.session.delete(self)
        banco.session.commit()