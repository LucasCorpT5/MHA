from flask_restful import Resource, reqparse
from models.usuario import UserModel

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
        atributos = reqparse.RequestParser()
