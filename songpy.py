#!usr/bin/python3

from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api

APP = Flask(__name__)
API = Api(APP, prefix="/dapi/v0")

# Upcoming code


@APP.route('/')
def index():
    return "Hello World"


@APP.route('/resource/<string:name>', methods=['GET'])
def get_resource(name = None):
    if name:
        return jsonify({'name': name})


@APP.errorhandler(404)
def not_found(error):
    print(error)
    return make_response(jsonify({'error': '404 Page not found'}), 404)


if __name__ == '__main__':
    APP.run(debug=True)
