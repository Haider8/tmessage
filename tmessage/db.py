"""Handles the connection to the SQLite database as well as DB interaction"""
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
APP.config['SQLALCHEMY_BINDS'] = {}
DB = SQLAlchemy(APP)


class Message(DB.Model):
    """ Database where messages will be stored """
    sender = DB.Column(DB.String(120), primary_key=True, nullable=False)
    message = DB.Column(DB.String(120), nullable=False)
    timestamp = DB.Column(DB.DateTime)

    def add(self):
        return 1+1
    def __repr__(self):
        return f"Message('{self.sender}','{self.message}','{self.timestamp}')"


def new_database(user):
    """ creates new database for new users """
    APP.config['SQLALCHEMY_BINDS'][user] = f'sqlite:///{user}.db'


def store_messages(user, raw_msg):
    """ function that stores messages from the particular user """
    Message.__bind_key__ = user
    time = datetime.now()
    DB.create_all()
    data = Message(sender=user, message=raw_msg, timestamp=time)
    DB.session.add(data)
    DB.session.commit()
