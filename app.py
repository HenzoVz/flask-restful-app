from flask import Flask
from flask_restful import Api
from resources.hotel import Hotel, Hoteis
app = Flask(__name__)
api = Api(app)

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<int:hotel_id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')
