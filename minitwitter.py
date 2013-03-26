#!/usr/bin/env python

import flask
from flask.ext.sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['DEBUG'] = True


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    time = db.Column(db.DateTime)


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
