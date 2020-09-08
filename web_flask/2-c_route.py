#!/usr/bin/python3
"""Flask framwework ligth weight"""

from flask import Flask
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
def hello_world_3():
    """hello world"""
    return 'C %s' % escape(username)


if __name__ == '__main__':
    app.run(debug=True)
