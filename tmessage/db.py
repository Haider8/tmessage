"""Handles the connection to the SQLite database as well as DB interaction"""
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
APP.config['SQLALCHEMY_BINDS'] = {}
DB = SQLAlchemy(APP)


class Message(DB.Model):
    def fun(user):
        __bind_key__ = user
    sender = DB.Column(DB.String(120), primary_key=True, nullable=False)
    message = DB.Column(DB.String(120), nullable=False)
    timestamp = DB.Column(DB.DateTime)

    def __repr__(self):
        return f"Message('{self.sender}','{self.message}','{self.timestamp}')"


def store_messages(user, raw_msg, new):
    """Store a message sent by the indicated user in the database"""
    if new == 'yes':
        APP.config['SQLALCHEMY_BINDS'][user] = f'sqlite:///{user}.db'

    Message.fun(user)
    time = datetime.now()
    DB.create_all()
    data = Message(sender=user, message=raw_msg, timestamp=time)
    DB.session.add(data)
    DB.session.commit()
