# user
from database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    # posts = db.relationship('Post', backref="author", lazy=True)
    
    # def __repr__(self):
    #     return f"User('{self.id}', '{self.username}', '{self.password}')"

