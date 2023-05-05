from typing import Dict, List, Optional
from flask import Flask, request, jsonify
import pathlib
from grove_rgb_lcd import *

app = Flask(__name__)
thisdir = pathlib.Path(__file__).parent.absolute() # path to directory of this file

def process_json(song_data):
    title = song_data['track']['title']
    artist = song_data['track']['subtitle']
    setText(f'{title[:15]}\n{artist[:15]}')

@app.route('/recognize', methods=['POST'])
def recognize_song():
    received = request.get_json()
    process_json(received)
    res = jsonify({})
    res.status_code = 201 # Status code for "created"
    return res

if __name__ == '__main__':
    app.run(host='172.20.10.6', port=5000)