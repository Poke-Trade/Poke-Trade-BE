# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "<h1>Home Page</h1>"
# # url route
# # custom route, allows dynamic urls
# @app.route('/home/<string:name>')
# def hello(name):
#     return f"Hello {name}"

# # id dynamic
# # @app.route('/home/<int:id>')
# # def hello(id):
# #     return f"Hello {name}"
# @app.route('/onlyget', methods=['GET'])
# def get_req():
#     return "You get only get this webpage!"

# # shows us actual errors
# if __name__ == "__main__":
#     app.run(debug=True)

