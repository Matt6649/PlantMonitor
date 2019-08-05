from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from time import ctime, sleep
import Adafruit_ADS1x15

app = Flask(__name__)
api = Api(app)

class Data(Resource):
    def get(self):
        hydration = Adafruit_ADS1x15.ADS1115().read_adc(0, gain=2/3)
        data = {'time': ctime(), 'hydration': hydration}
        return jsonify(data)

api.add_resource(Data, '/data')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port='80')
