#!/usr/bin/python3
""" has routes / and /hbnb"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ returns "Hello HBNB" """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_HBNB():
    """ returns "HBNB" """
    return "HBNB"


if __name__ == "__main__":
    app.run()
