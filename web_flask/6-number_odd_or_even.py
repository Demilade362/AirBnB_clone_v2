#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ display Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ display HBNB """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ display C with <text> value """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ display python with <text> value """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ display <n> is a number only if <n> is an integer """
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ display HTML page only if <n> is an integer """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ display HTML page only if <n> is an integer """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
