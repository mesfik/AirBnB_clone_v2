#!/usr/bin/python3
"""
flask web application module
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from operator import attrgetter


app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def state_list():
    """
    a function to display states id and name
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown():
    """ closing the sqlAlchemy"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
