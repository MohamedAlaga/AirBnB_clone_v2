#!/usr/bin/python3
""" first flask app """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ returns Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/', strict_slashes=False)
def hbnb():
    """ returns HBNB """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
