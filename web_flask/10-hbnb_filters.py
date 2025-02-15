#!/usr/bin/python3
"""Module containing hbnb filter route"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def fetch_states():
    """Hbnb filter function"""
    states_list = []
    a_s = {}
    all_states = storage.all(State)
    all_cities = storage.all(City)
    all_amenities = storage.all(Amenity)
    for st in all_states:
        a_s_d = {}
        ct_list = []
        for ct in all_cities:
            if all_cities[ct].state_id == all_states[st].id:
                tmp = {}
                tmp['name'] = all_cities[ct].name
                ct_list.append(tmp)
        a_s_d['name'] = all_states[st].name
        sorted_cts = sorted(ct_list, key=lambda x: x['name'])
        a_s_d['cities'] = sorted_cts
        states_list.append(a_s_d)
    sorted_states = sorted(states_list, key=lambda x: x['name'])
    am_s = []
    for am in all_amenities:
        am_s.append(all_amenities[am].name)
    sorted_amenities = am_s.sort()
    a_s['states'] = sorted_states
    a_s['amenities'] = sorted_amenities
    return render_template('10-hbnb_filters.html', a_s=a_s)


@app.teardown_appcontext
def app_teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run()
