#!/usr/bin/python3
"""
defines the route /state_list
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def teardown(self):
    """
    closes and starts a sql session
    """
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    returns a html page of all states for routes /states_list
    """
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)

if __name__ == '__main__':
    app.run()
