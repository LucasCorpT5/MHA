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

    def json(self):
        return {
            'user_id': user_id,
            'nome': self.nome
        }

    @classmethod
    def find_user(cls):
        user = cls.query.filter_by(user_id=user_id).first()
        if user:
            return user
        else:
            return None
