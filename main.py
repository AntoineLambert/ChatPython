#!/usr/bin/python
# -*- coding: utf-8 -*-
import rethinkdb as r
from flask import Flask, render_template
from flask_socketio import SocketIO
from threading import Thread
#initialise le serveur sockio avec Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

#se connecter à RethinkDB
r.connect( "localhost", 28015).repl()




print('🐱')

if __name__ == '__main__':
    socketio.run(app)