#!/usr/bin/python3
"""
contains route definitions
'/python/', '/python/<text>', '/', '/hbnb' and '/c/<text>'
"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """route returns 'Hello HBNB'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_HBNB():
    """route returns 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_route(text):
    """route returns 'C <text>'"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_route(text=None):
    """routes returns 'Python <text>' or Python is cool"""
    if text is None:
        return "Python is cool"
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """returns '<n> is a number' """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ returns a html page 5-number.html"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run()
