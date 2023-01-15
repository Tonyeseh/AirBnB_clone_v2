#!/usr/bin/python3
"""
contains route definitions '/', '/hbnb' and '/c/<text>'
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """route returns 'Hello HBNB'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_HBNB():
    """route returns 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>')
def C_route(text):
    """route returns 'C <text>'"""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run()
