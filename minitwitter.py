#!/usr/bin/env python

import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def home():
    return "Hello World!"


@app.route('/new', methods=['GET', 'POST'])
def new():
    if flask.request.method == 'POST':
        print "new message:", flask.request.form['message']
        return flask.redirect(flask.url_for('home'))
    return flask.render_template('new.html')


if __name__ == '__main__':
    app.run()
