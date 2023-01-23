#!/usr/bin/python3
"""
defines the route /cities_by_states
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

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
	"""
	returns a html page of all states for routes /states_list
	"""
	states = storage.all('State').values()
	return render_template('8-cities_by_states.html', states=states)

if __name__ == '__main__':
	app.run()
