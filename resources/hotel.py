from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
    {
    'hotel_id': 'alpha',
    'nome': 'alpha hotel',
    'estrelas': 4.3,
    'diaria': 420.34,
    'cidade': 'Curitiba'
    },
    {
    'hotel_id': 'esmeralda',
    'nome': 'esmeralda hotel',
    'estrelas': 4.5,
    'diaria': 450.22,
    'cidade': 'São Paulo'
    },
    {
    'hotel_id': 'reilly',
    'nome': 'reilly hotel',
    'estrelas': 3.9,
    'diaria': 310.44,
    'cidade': 'Minas Gerais'
    }

]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel not found'}, 404 # not found

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'message': "Hotel id '{}' already exists".format(hotel_id)}, 400 # bad request

        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()
        return hotel.json()

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()

        hotel_encontrado = HotelModel.find_hotel(hotel_id, **dados)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            return hotel, 200 # Ok
        else:
            hoteis.save(novo_hotel)
            return novo_hotel, 201 # Created

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel deleted.'}
