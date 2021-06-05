from flask import Flask
from flask_request import Resource, Api

app = Flask(__name__)
api = Api(app)


class Health(Resource):
    def get(self):
        resp = {'status': 200, 'msg': 'SUCCESS_OK'}
        return resp, 200


api.add_resource(Health, 'health/status')

app.run(port=5000, debug=True)
