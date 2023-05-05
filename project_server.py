# Server runs on RPi

from typing import Dict, List, Optional
from flask import Flask, request, jsonify
import pathlib
from grove_rgb_lcd import *

# Define Flask server
app = Flask(__name__)
thisdir = pathlib.Path(__file__).parent.absolute() # path to directory of this file

# Function to process the json data received by the server
def process_json(song_data):
    # Parse the json for the title and artist using dictionary indexing
    title = song_data['track']['title']
    artist = song_data['track']['subtitle']
    # Write the title and artist to the LCD
    setText(f'{title[:15]}\n{artist[:15]}')

# Route to the '/recognize' path on the Flask server. Upon receiving data from a client POST request, process it and
# send back a 'success' status code.
@app.route('/recognize', methods=['POST'])
def recognize_song():
    received = request.get_json()
    process_json(received)
    res = jsonify({})
    res.status_code = 201 # Status code for "created"
    return res

if __name__ == '__main__':
    app.run(host='172.20.10.6', port=5000)