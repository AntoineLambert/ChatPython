#!/usr/bin/python
# -*- coding: utf-8 -*-
import rethinkdb as r
import flask
from flask import Flask, render_template, request
from flask_socketio import SocketIO
from threading import Thread
#initialise le serveur sockio avec Flask
app = flask.Flask(__name__)

#se connecter à RethinkDB
conn = r.connect( "localhost", 28015).repl()

@app.route('/')
def my_form():
	return flask.render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():

	text = request.form['text']
	print text
	r.db("chatDB").table("message").insert(text).run(conn)
	return my_form()
	
print('🐱')

if __name__ == '__main__':
    app.run()