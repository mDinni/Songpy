#!usr/bin/python3

import lxml
import json
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response


APP = Flask(__name__)
API = Api(APP, prefix="/dapi/v0")

def search_song(name):
    DOMAIN = "https://www.youtube.com/"
    URL = "https://www.youtube.com/results?search_query="
    PRED = "<CONVERTER>"

    # Getting song name from the user
    song_name = name

    # Creating the link for query
    query = URL + song_name.replace(' ', '+')

    # Parsing the song from the searched page
    res = requests.get(query)
    data = res.content
    soup = BeautifulSoup(data, 'lxml')
    rel = soup.find(attrs={'class': 'yt-uix-tile-link'})['href']
    url = PRED + urljoin(DOMAIN, rel)

    # Getting song from the parsed query
    song_res = requests.get(url)
    raw_data = song_res.content
    try:
        song = json.loads(raw_data)
        return song
    except ValueError:
        return {"link": False, "message": "No such song found"}


# Upcoming code

@APP.route('/')
def index():
    return "Hello World"


@APP.route('/resource/<string:name>', methods=['GET'])
def get_resource(name=None):
    if name:
        song = search_song(name)
        return jsonify({'song': song})


@APP.errorhandler(404)
def not_found(error):
    print(error)
    return make_response(jsonify({'error': '404 Page not found'}), 404)


if __name__ == '__main__':
    APP.run(debug=True)
