#!/usr/bin/python
# -*- coding: utf-8 -*-
import rethinkdb as r
from flask import Flask, render_template
from flask_socketio import SocketIO
#initialise le serveur sockio avec Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
#crée la Table sur RethinkDB
r.connect( "localhost", 28015).repl()
r.db_create('chatDB').run()
r.db("chatDB").table_create("name").run()
r.db("chatDB").table_create("message").run()
r.db("chatDB").table_create("time").run()


print('Hello World !')


if __name__ == '__main__':
    socketio.run(app)