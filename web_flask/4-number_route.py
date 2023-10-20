#!/usr/bin/python3
"""Hello Flask route declaration module second endpoint"""

from flask import Flask

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


if __name__ == '__main__':
    app.run()
