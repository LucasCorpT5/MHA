from flask_restful import Resource


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
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message': 'Hotel not found'}, 404 # not found

    def post(self, hotel_id):
        pass

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass
