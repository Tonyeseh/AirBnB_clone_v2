"""
Contains a route that returns a string
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
        / route that returns "Hello HBNB!"
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run()
