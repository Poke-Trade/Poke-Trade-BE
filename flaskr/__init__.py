from flask import Flask, render_template, redirect, url_for, request

# app = Flask(__name__)

import os

# from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    def create_app():
        from . import db
        db.init_app(app)
        return app
    return app


@app.route('/api/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials'
    else:
        return redirect(url_for('/'))
    # response = {'error': "Not implemented"}
    return render_template('authtest.html', error=error)


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
