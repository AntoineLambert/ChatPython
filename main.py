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
                       TABLE_NAME='messages',
                       TABLE_ACCOUNT='account'))

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

@app.route('/', methods=['GET', 'POST'])
def main():
	if request.method == 'POST':
		if request.form['submit'] == 'SignUp':
			print('Signup')
			def inscription():
				name = request.form['name']
				password = request.form['password']
				email = request.form['email']
				if request.method == 'POST':
					rdb.db(app.config['DB_NAME']).table(app.config['TABLE_ACCOUNT']).insert({'name': name, 'password': password, 'email': email}).run(g.conn)
			return my_form()
		elif request.form['submit'] == 'SignIn':
			print('Signin')
			def my_form_post():
				print('WIN!')
				error = None
				name = request.form['name']
				password = request.form['password']
				email = request.form['email']
				if request.method == 'POST':
					rdb.db(app.config['DB_NAME']).table(app.config['TABLE_ACCOUNT']).filter({'name': name, 'password': password}).run(g.conn)
					
					if name != 'name' or password != 'password':
						error = "Mauvais Mot de Passe !"
					else:
						print('Réussi !')
			return my_form()

		elif request.form['submit'] == 'Send':
			print('Send')
			def my_form_post():
				if request.method == 'POST':
					text = request.form['text']
					print text
					rdb.db(app.config['DB_NAME']).table(app.config['TABLE_NAME']).insert({'text': text}).run(g.conn)
			return my_form()


	print('🐱')

if __name__ == '__main__':
    app.run()
