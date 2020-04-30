# where we initilize the application - Think app.js
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os


app = Flask(__name__)
# secret key
JWT_SECRET = os.getenv("SECRET")
# initiate sqllite db
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
# # pass app into sql db
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from database import routes, adventure
