# where we initilize the application - Think app.js
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os


app = Flask(__name__)
# secret key
JWT_SECRET = os.getenv("SECRET")
# initiate sqllite db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# pass app into sql db
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from database import routes
