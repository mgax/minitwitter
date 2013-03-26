#!/usr/bin/env python

import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def home():
    return "Hello World!"


@app.route('/new')
def new():
    return flask.render_template('new.html')


if __name__ == '__main__':
    app.run()
