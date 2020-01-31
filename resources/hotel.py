from flask_restful import Resource, reqparse
from db_json.data_base import DB
from models.hotel import HotelModel


class Hoteis(Resource):
    def get(self):
        if len(DB.read()['hoteis']) > 0:
            return {'hoteis': list(map(lambda hotel: hotel, DB.read()['hoteis']))}, 200
        return {'message': 'Hoteis not found'}, 404

class Hotel(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    db = DB.read()

    @staticmethod
    def find(hotel_id):
        for hotel in Hotel.db['hoteis']:
            if hotel['id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = Hotel.find(hotel_id)
        if hotel:
            return hotel
        return {'message': 'Hotel not found'}, 404

    def post(self, hotel_id):

        hotel_id = len(Hotel.db['hoteis']) + 1
        dados = Hotel.argumentos.parse_args()
        hto = HotelModel(hotel_id, **dados)
        novo_hotel = hto.json()
        if hotel_id != Hotel.db['id']:
            Hotel.db['hoteis'].append(novo_hotel)
            DB.save(Hotel.db)
            return novo_hotel, 200
        return {'message': str(hotel_id) + 'existing'}

    def put(self, hotel_id):

        dados = Hotel.argumentos.parse_args()
        hto = HotelModel(hotel_id, **dados)
        novo_hotel = hto.json()
        hotel = Hotel.find(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            Hotel.db['hoteis'].append(hotel)
            DB.save(Hotel.db)
            return novo_hotel, 200
        return {'message': 'Hotel not found'}, 404

    def delete(self, hotel_id):

        hotel = Hotel.find(hotel_id)
        if hotel:
            Hotel.db['hoteis'].pop(hotel['id'] - 1)
            DB.save(Hotel.db)
            return {'message': 'hotel successfully deleted'}, 200
        return {'message': 'Hotel not found'}, 404