#!/usr/bin/python
# -*- coding: utf-8 -*-
import rethinkdb as rdb
import flask
from flask import Flask, request, redirect, flash, render_template, url_for
from flask import g, jsonify, render_template, request, abort, make_response, session
from flask_socketio import SocketIO
from threading import Thread
import json
#initialise le serveur sockio avec Flask
app = Flask(__name__, static_url_path='')
app.config.from_object(__name__)

app.config.update(dict(DEBUG=True,
                       RDB_HOST='localhost',
                       RDB_PORT=28015,
                       DB_NAME='chatDB',
                       TABLE_NAME='messages'))

# open connection before each request
@app.before_request
def before_request():
    try:
        g.conn = rdb.connect(host=app.config['RDB_HOST'], port=app.config['RDB_PORT'], db=app.config['DB_NAME'])
    except RqlDriverError:
        abort(503, "Database connection could be established.")

@app.teardown_request
def teardown_request(exeption):
	try:
		g.conn.close()
	except AttributeError:
		pass

@app.route('/')
def my_form():
	return flask.render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['text']
	print text
	rdb.db(app.config['DB_NAME']).table(app.config['TABLE_NAME']).insert({'text': text}).run(g.conn)
	return my_form()

print('🐱')

if __name__ == '__main__':
    app.run()
