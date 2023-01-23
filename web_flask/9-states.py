#!/usr/bin/python3
"""
defines the route /states
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """
    closes db session
    """
    storage.close()


@app.route('/states/', strict_slashes=False)
def states():
    """route to all states"""
    states = storage.all('State').values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """displays a state with it's cities"""
    states = storage.all('State')
    unique_state = None
    for state in states.values():
        if state.id == id:
            unique_state = state
            break
    if unique_state:
        return render_template('9-states.html', state=unique_state)
    else:
        return render_template('9-states.html', error='Not Found!')


if __name__ == '__main__':
    app.run()
