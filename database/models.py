# user
from database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    # posts = db.relationship('Post', backref="author", lazy=True)
    
    # def __repr__(self):
    #     return f"User('{self.id}', '{self.username}', '{self.password}')"

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    x = db.Column(db.Integer, nullable=True)
    y = db.Column(db.Integer, nullable=True)  
    item = db.relationship('Item', backref = "room", lazy=True)

    def __init__(self, name, description, x, y, item=None):
        self.name = name
        self.description = description
        self.x = x
        self.y = y
        self.item = item if item is not None else []

    def __str__(self):
        return f"{self.name}, {self.description}, {self.x}, {self.y}, {self.item}"
    

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    player_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    room_id   = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=True)


    def __init__(self, name, description, player_id=None, room_id=None):
        self.name = name
        self.description = description
        self.player_id = player_id
        self.room_id = room_id

    def __str__(self):
        return f"{self.name}, {self.description}, {player_id}, {room_id}"
    
      



