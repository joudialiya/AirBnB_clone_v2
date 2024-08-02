#!/usr/bin/python3
'''Hello world app'''

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    '''Route handler'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''Route handler'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    '''Route handler'''
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
