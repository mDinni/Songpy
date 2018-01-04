#!usr/bin/python3

from flask import Flask
from flask_restful import Resource, Api

APP = Flask(__name__)
API = Api(APP, prefix="/dapi/v0")

# Upcoming code

if __name__ == '__main__':
    APP.run(debug=True)
