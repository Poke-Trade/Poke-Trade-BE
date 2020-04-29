# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SECRET_KEY'] = "secret"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)
#     # posts = db.relationship('Post', backref="author", lazy=True)
    
#     def __repr__(self):
#         return f"User('{self.id}', '{self.username}', '{self.password}')"



# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


# if __name__ == '__main__':
#     app.run(debug=True)

