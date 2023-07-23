#!/usr/bin/python3
"""
a web framework module that listens 0.0.0.0 port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello():
    """
    a function that display's hello HBNB
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    a function that displays HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_is_fun(text):
    """
    afunction that displays C followed by value
    of the text!
    """
    text = text.replace('_', ' ')
    return ("C " + text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_txt(text):
    """
    a function that displays python + text
    Args: text - the text next to the word python
    Return: python + text
    """
    text = text.replace('_', ' ')
    return ("Python " + text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_integer(n):
    """
    a function that displays n is a number
    Args:
         n - is an integer number
    Return: n is a number
    """
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
