#!/usr/bin/python3
"""
flask web application module
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def state():
    """
    a function to display cities by states
    """
    states = storage.all(State).values()
    return render_template("9-states.html", state=states)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """
    a function display a HTML page: (inside the tag BODY)
    Args: id - the id of state
    Return: the rendered template
    """
    for state in storage.all(State).values():
        if (state.id == id):
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(error):
    """ closing the sqlAlchemy"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
