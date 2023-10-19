#!/usr/bin/python3
"""Hello Flask route declaration module second endpoint"""

from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Root route for Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def only_hbnb():
    """/hbnb route definition"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_arg_hbnb(text):
    """/c/<text> route definition"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_arg_hbnb(text="is cool"):
    """/python/<text> route definition"""
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<n>", strict_slashes=False)
def int_arg_hbnb(n):
    """/number/<n> route definition"""
    try:
        if isinstance(int(n), int):
            return "{} is a number".format(n)
        abort(404)
    except ValueError:
        pass
    abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def int_tmpl_arg_hbnb(n):
    """/number_template/<n> route definition"""
    try:
        if isinstance(int(n), int):
            return render_template('5-number.html', n=n)
        abort(404)
    except ValueError:
        pass
    abort(404)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def int_tmpl_odd_even_arg_hbnb(n):
    """/number_odd_or_even/<n> route definition"""
    try:
        n_int = int(n)
        if isinstance(n_int, int):
            if n_int % 2 == 0:
                odd_eve = 'even'
            else:
                odd_eve = 'odd'
            return render_template('6-number_odd_or_even.html', n=n, p=odd_eve)
        abort(404)
    except ValueError:
        pass
    abort(404)


if __name__ == '__main__':
    app.run()
