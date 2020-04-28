import hashlib
import json
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request, render_template, make_response

from room import Room
from player import Player
from world import World
from items import Item, Food, Weapon
from store import Store

app = Flask(__name__)

def login():
    values = request.get_json()
    required = ['username', 'password']

    if not all(k in values for k in required):
        response = {'message': "Missing Values"}
        return jsonify(response), 400

    username = values.get('username')
    password = values.get('password')

    response = world.authenticate_user(username, password)
    if response is None:
        return jsonify(response), 500
    else:
        return jsonify(response), 200