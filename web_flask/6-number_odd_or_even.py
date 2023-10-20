#!/usr/bin/python3
"""Hello Flask route declaration module second endpoint"""

from flask import Flask, render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def int_arg_hbnb(n):
    """/number/<n> route definition"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def int_tmpl_arg_hbnb(n):
    """/number_template/<n> route definition"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def int_tmpl_odd_even_arg_hbnb(n):
    """/number_odd_or_even/<n> route definition"""
    if int(n) % 2 == 0:
        odd_eve = 'even'
    else:
        odd_eve = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, p=odd_eve)


if __name__ == '__main__':
    app.run()
