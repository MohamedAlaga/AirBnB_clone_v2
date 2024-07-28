#!/usr/bin/python3
""" first flask app """
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ returns Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ c and text """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """ python and text """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_text(n):
    """ replace with int only if given int. """
    n = str(n)
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ replace with int only if given int. """
    n = str(n)
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
