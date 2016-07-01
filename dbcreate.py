#!/usr/bin/python
# -*- coding: utf-8 -*-
import rethinkdb as r
from flask import Flask, render_template
#initialise le serveur sockio avec Flask
app = Flask(__name__)
#crée la Table sur RethinkDB
r.connect( "localhost", 28015).repl()
r.db_create('chatDB').run()
r.db("chatDB").table_create("account").run()
r.db("chatDB").table_create("messages").run()

print('🐱')

if __name__ == '__main__':
    app.run()
