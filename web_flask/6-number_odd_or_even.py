#!/usr/bin/python3
"""Flask framwework ligth weight"""

from flask import Flask
from markupsafe import escape
from flask import render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """hello world"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_world_2():
    """hello world"""
    return 'HBNB'


@app.route('/c/<text>')
def hello_world_3(text):
    """hello world"""
    return 'C %s' % escape(text.replace('_', ' '))


@app.route("/python/", defaults={"text": "is cool"})
@app.route('/python/<text>')
def hello_world_4(text='is cool'):
    """hello world"""
    return 'Python %s' % escape(text.replace('_', ' '))


@app.route('/number/<int:n>')
def hello_world_5(n):
    """hello world"""
    return '%s is a number' % n


@app.route('/number_template/<int:n>')
def hello_world_6(n):
    """hello world"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def hello_world_7(n):
    """hello world"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(debug=True)
