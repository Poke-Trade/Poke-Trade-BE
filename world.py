from room import Room
from player import Player
from grid import Grid
import random
import math
import bcrypt


class World:
    def __init__(self):
        self.starting_room = None
        self.rooms = {}
        self.players = {}
        self.create_world()
        self.password_salt = bcrypt.gensalt()

    def add_player(self, username, password1, password2):
        if password1 != password2:
            return {'error': "Passwords do not match"}
        elif len(username) <= 2:
            return {'error': "Username must be longer than 2 characters"}
        elif len(password1) <= 5:
            return {'error': "Password must be longer than 5 characters"}
        elif self.get_player_by_username(username) is not None:
            return {'error': "Username already exists"}
        password_hash = bcrypt.hashpw(password1.encode(), self.password_salt)
        player = Player(username, self.starting_room, password_hash)
        self.players[player.auth_key] = player
        return {'key': player.auth_key}

    def get_player_by_auth(self, auth_key):
        if auth_key in self.players:
            return self.players[auth_key]
        else:
            return None

    def get_player_by_username(self, username):
        for auth_key in self.players:
            if self.players[auth_key].username == username:
                return self.players[auth_key]
        return None

    def authenticate_user(self, username, password):
        user = self.get_player_by_username(username)
        if user is None:
            return None
        password_hash = bcrypt.hashpw(password.encode(), self.password_salt)
        if user.password_hash == password_hash:
            return user
        return None

    # UNDERSTAND
    #   Build a grid filled up by rooms
    #   Need to have a perimeter and a be be able to hold 100 rooms

    def create_world(self):
        # Generate 100 rooms in a 10x10 grid style
        # generate them first, then connect them all together
        grid_map = Grid(100)
        grid_map.create_grid(10, 10, 100)
        self.rooms = grid_map.rooms
        # print(grid_map.rooms)
        # num_rooms = 100
        # rows = 10
        # columns = 10
        # id = 0
        # x = 0
        # y = 0

        # rooms = []
        # for col in range(columns):
        #     for row in range(rows):
        #         name = "name" + "1"
        #         description = "new name"
        #         x = col
        #         y = row
        #         room = Room(name, description, id, x, y)
        #         self.rooms[id] = room
        #         rooms.append(room)
        #         id += 1
        #         rooms.append(room)

        # # print(rooms)
        # self.starting_room = self.rooms[0]
        # # connect all the rooms in grid style
        # id = 0
        # for row in range(rows):
        #     for col in range(columns):
        #         room = self.rooms[id]
        #         if row - 1 >= 0:
        #             room_n = self.rooms[col + (row - 1) * 10]
        #             room.n_to = room_n
        #         if col + 1 < 10:
        #             room_e = self.rooms[col + 1 + row * 10]
        #             room.e_to = room_e
        #         if row + 1 < 10:
        #             room_s = self.rooms[col + (row + 1) * 10]
        #             room.s_to = room_s
        #         if col - 1 >= 0:
        #             room_w = self.rooms[col - 1 + row * 10]
        #             room.w_to = room_w
        #         print("roomId ", room.id, "\nx", room.x, "\ny", room.y,
        #               room.n_to.id if room.n_to is not None else None,
        #               room.e_to.id if room.e_to is not None else None,
        #               room.s_to.id if room.s_to is not None else None,
        #               room.w_to.id if room.w_to is not None else None
        #               )
        #         id += 1


num_rooms = 25  # max number of rooms to use
width = 5  # X-axis length
height = 5  # Y-axis length
room_id = 0  # will rep the ACTUAL ID
grid = [None] * height
w = World()
num_rooms = 25
# width = 8
# height = 7
print(w.create_world())
# print(w)
# Link rooms together
# starting room

# self.rooms = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons", 1, 1, 1),

#     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east.""", 2, 1, 2),

#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm.""", 3, 1, 3),

#     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air.""", 4, 2, 2),

#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south.""", 5, 2, 3),
# }

# self.rooms['outside'].connect_rooms('n', self.rooms['foyer'])
# self.rooms['foyer'].connect_rooms('n', self.rooms['overlook'])
# self.rooms['foyer'].connect_rooms('e', self.rooms['narrow'])
# self.rooms['narrow'].connect_rooms('n', self.rooms['treasure'])

# self.starting_room = self.rooms['outside']
