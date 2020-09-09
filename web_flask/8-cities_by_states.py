#!/usr/bin/python3
"""Flask framwework ligth weight"""

from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def pop_db(x):
    """storage closing"""
    storage.close()


@app.route('/states_list')
def hello_world_6():
    """hello world"""
    state = list(storage.all(State).values())
    return render_template('7-states_list.html', state=state)


@app.route('/cities_by_states')
def hello_world_7():
    """hello world"""
    state = list(storage.all(State).values())
    return render_template('8-cities_by_states.html', state=state)




if __name__ == '__main__':
    app.run(debug=True)
    storage.reload()
