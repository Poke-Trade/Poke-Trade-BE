import hashlib
import json
from time import time
from uuid import uuid4
import bcrypt

from flask import Flask, jsonify, request, render_template, make_response
# from pusher import Pusher
# from decouple import config

from database.room import Room
from database.player import Player
from database.world import World
from database import app, db


# # Look up decouple for config variables
# pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config(
#     'PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))


world = World()

world.create_world()
all_rooms = list(world.rooms)
starting_room = all_rooms[0]
app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response


def get_player_by_header(world, auth_header):
    if auth_header is None:
        return None

    auth_key = auth_header.split(" ")
    if auth_key[0] != "Token" or len(auth_key) != 2:
        return None

    player = world.get_player_by_auth(auth_key[1])
    return player


@app.route('/api/adv/init/', methods=['GET'])
def init():
    player = get_player_by_header(world, request.headers.get("Authorization"))
    if player is None:
        response = {'error': "Malformed auth header"}
        return jsonify(response), 500

    response = {
        'title': player.current_room.name,
        'description': player.current_room.description,
    }
    return jsonify(response), 200


@app.route('/api/adv/move/', methods=['POST'])
def move():
    # player = get_player_by_header(world, request.headers.get("Authorization"))
    # if player is None:
    #     response = {'error': "Malformed auth header"}
    #     return jsonify(response), 500
    player = Player("aj", starting_room, "password")
    values = request.get_json()
    required = ['direction']
    next_room_id = None
    print("current room ", player.current_room.name)

    if not all(k in values for k in required):
        response = {'message': "Missing Values"}
        return jsonify(response), 400

    direction = values.get('direction')
    print("\nDirection --> ", direction)
    room = player.current_room
    if direction == "n":
        next_room_id = room.n_to
        print("\nNext Room -->", next_room_id)
    elif direction == "s":
        next_room_id = room.s_to 
    if next_room_id is not None or next_room_id > 0:
        next_room = room.get_room_in_direction(direction)
        print("NEXT ROOM -->", next_room.name, next_room.id)
        player.current_room = next_room
        print("Room change --> ", player.current_room.name)
        response = {
            'next': next_room,
            'title': player.current_room.name,
            'description': player.current_room.description,
            'id': player.current_room.id
        }
        return jsonify(response), 200
    else:
        response = {
            'error': "You cannot move in that direction.",
        }
        return jsonify(response), 500
    
        



@app.route('/api/adv/take/', methods=['POST'])
def take_item():
    # IMPLEMENT THIS
    response = {'error': "Not implemented"}
    return jsonify(response), 400


@app.route('/api/adv/drop/', methods=['POST'])
def drop_item():
    # IMPLEMENT THIS
    response = {'error': "Not implemented"}
    return jsonify(response), 400


@app.route('/api/adv/inventory/', methods=['GET'])
def inventory():
    # IMPLEMENT THIS
    response = {'error': "Not implemented"}
    return jsonify(response), 400


@app.route('/api/adv/buy/', methods=['POST'])
def buy_item():
    # IMPLEMENT THIS
    response = {'error': "Not implemented"}
    return jsonify(response), 400


@app.route('/api/adv/sell/', methods=['POST'])
def sell_item():
    # IMPLEMENT THIS
    response = {'error': "Not implemented"}
    return jsonify(response), 400


@app.route('/api/adv/rooms/', methods=['GET'])
def rooms():
    iterable = []
    for room in world.rooms:
        # print(room)
        room_dict = dict(room.__dict__)
        # print(room_dict)
        room_dict['n_to'] = room.n_to.id if room.n_to is not None else ""
        room_dict['e_to'] = room.e_to.id if room.e_to is not None else ""
        room_dict['s_to'] = room.s_to.id if room.s_to is not None else ""
        room_dict['w_to'] = room.w_to.id if room.w_to is not None else ""
        iterable.append(room_dict)
    response = {'rooms': iterable}
    return jsonify(response), 200


# Run the program on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
