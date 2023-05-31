from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

GAMES = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Tiny Epic Galaxies',
        'designer': 'Scott Almes',
        'publisher': 'Gamelyn Games',
        'played': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Imhotep',
        'designer': 'Phil Walker-Harding',
        'publisher': 'KOSMOS',
        'played': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Carcassonne',
        'designer': 'Klaus-Jürgen Wrede',
        'publisher': 'Hans im Glück',
        'played': True
    }
]

@app.route('/games', methods=['GET', 'POST'])
def all_games():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'designer': post_data.get('designer'),
            'publisher': post_data.get('publisher'),
            'played': post_data.get('played')
        })
        response_object['message'] = 'Game added!'
    else:
        response_object['games'] = GAMES
    return jsonify(response_object)

@app.route('/games/<game_id>', methods=['PUT', 'DELETE'])
def single_game(game_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_game(game_id)
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'designer': post_data.get('designer'),
            'publisher': post_data.get('publisher'),
            'played': post_data.get('played')
        })
        response_object['message'] = 'Game updated!'
    if request.method == 'DELETE':
        remove_game(game_id)
        response_object['message'] = 'Game removed!'
    return jsonify(response_object)

def remove_game(game_id):
    for game in GAMES:
        if game['id'] == game_id:
            GAMES.remove(game)
            return True
    return False

if __name__ == '__main__':
    app.run()