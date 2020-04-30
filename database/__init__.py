# where we initilize the application - Think app.js
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv


app = Flask(__name__)
print('testing db url', os.getenv('DATABASE_URL'))
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)


# secret key
JWT_SECRET = os.getenv("SECRET")
# initiate sqllite db
app.config['SECRET_KEY'] = 'secret'

# # pass app into sql db

bcrypt = Bcrypt(app)


from database import routes, adventure
