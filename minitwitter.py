#!/usr/bin/env python

from datetime import datetime
import times
import flask
from flask.ext.sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
db = SQLAlchemy(app)
app.config.from_pyfile('settings.py')


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    time = db.Column(db.DateTime)


@app.template_filter()
def local_time_format(value):
    return times.format(value, timezone='EET', fmt='%d %b %Y, %H:%M:%S')


@app.before_request
def get_user():
    flask.g.username = flask.session.get('username')


@app.route('/')
def home():
    return flask.render_template('messages.html', messages=Message.query.all())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if flask.request.method == 'POST':
        text = flask.request.form['message']
        message = Message(text=text, time=datetime.utcnow())
        db.session.add(message)
        db.session.commit()
        flask.flash("Message saved")
        return flask.redirect(flask.url_for('home'))
    return flask.render_template('new.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        flask.session['username'] = username
        flask.flash("welcome, %s" % username)
        return flask.redirect(flask.url_for('home'))
    return flask.render_template('login.html')


@app.route('/logout')
def logout():
    flask.session.pop('username', '')
    flask.flash("bye!")
    return flask.redirect(flask.url_for('home'))


if __name__ == '__main__':
    db.create_all()
    app.run()
