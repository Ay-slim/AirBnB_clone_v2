#!/usr/bin/python3
"""Module containing list_state route"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def fetch_states():
    """Fetch states function definition"""
    all_states = storage.all(State)
    return render_template('7-states_list.html', a_s=all_states)


@app.teardown_appcontext
def app_teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run()
