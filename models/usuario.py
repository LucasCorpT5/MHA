from sql_alchemy import banco

class UserModel(banco.Model):
    __tablename__ = "users"

    user_id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(40))
    email = banco.Column(banco.String(40))
    senha = banco.Column(banco.String(40))

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
