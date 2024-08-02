#!/usr/bin/python3
'''Hello world app'''

import flask


app = flask.Flask(__name__, )


@app.route("/", strict_slashes=False)
def hello():
    '''Route handler'''
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
