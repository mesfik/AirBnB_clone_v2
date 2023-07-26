#!/usr/bin/python3
"""
flask web application module
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


def cities_att(state):
    """
    a function To load all cities of a State
    """
    if hasattr(storage, 'cities'):
        cities = sorted(state.cities, key=lambda k: k.name)
    else:
        cities = sorted(state.cities, key=lambda k: k.name)
    return cities


app.jinja_env.globals['cities_att'] = cities_att


@app.route('/cities_by_states', strict_slashes=False)
def city_list():
    """
    a function to display cities by states
    """
    states = storage.all(State).values()
    states_sort = sorted(states, key=lambda k: k.name)
    return render_template("8-cities_by_states.html", states=states_sort)


@app.teardown_appcontext
def teardown(error):
    """ closing the sqlAlchemy"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
