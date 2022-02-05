from flask_restful import Resource, reqparse
from models.usuario import UserModel

atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help="The field 'login' cannot be left blank")
atributos.add_argument('senha', type=str, required=True, help="The field 'senha' cannot be left blank")

class User(Resource):
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        else:
            return {'message': 'User not found'}, 404

    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            user.delete_user()
            return {'messsage': 'User deleted'}
        else:
            return {'message': 'User not found'}, 404

class UserRegister(Resource):
    def post(self):
        dados = atributos.parse_args()

        if UserModel.find_by_login(dados['login']):
            return {'message': "The login '{}' already exists.".format(dados['login'])}

        user = UserModel(**dados)
        user.save_user()
        return {'message': 'User created successfully!'}, 201 # Created

class UserLogin(Resource):
    @classmethod
    def post(cls):
        dados = atributos.parse_args()

        user = UserModel.find_by_login(dados['login'])

        if user and safe_str_cmp(user.senha, dados['senha']):
            pass
