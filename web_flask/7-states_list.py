#!/usr/bin/python3
""" module 7-states_list """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def get_all_states():
    """ returns a template with all states """
    return render_template('7-states_list.html', states=storage.all("State").values())


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
