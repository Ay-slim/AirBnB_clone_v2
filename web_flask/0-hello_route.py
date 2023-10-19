#!/usr/bin/python3
"""Hello Flask route declaration module"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Hello HBNB function definition"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run()
