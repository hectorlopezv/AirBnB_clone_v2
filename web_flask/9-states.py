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

@app.route("/states")
def hello_1():
    """hello display all states like usual"""
    state = storage.all(State)
    return render_template('9-states.html', state=state)
       

@app.route("/states/<id>")
def hello_2(id):
    """return dict if id found else ..."""
    for jsn in storage.all(State).values():
         if jsn.id == id:
            return render_template('9-states.html', state=jsn)
    return render_template('9-states.html')
 

if __name__ == '__main__':
    app.run(debug=True)
    storage.reload()
    app.run(host='0.0.0.0', port='5000')
