"""Handles the connection to the SQLite database as well as DB interaction"""
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
APP.config['SQLALCHEMY_BINDS'] = {}
DB = SQLAlchemy(APP)

USER = ''


class Message(DB.Model):
    __bind_key__ = USER
    sender = DB.Column(DB.String(120), primary_key=True, nullable=False)
    message = DB.Column(DB.String(120), nullable=False)
    timestamp = DB.Column(DB.DateTime)

    def __repr__(self):
        return f"Message('{self.sender}','{self.message}','{self.timestamp}')"


def store_messages(user, raw_msg, new):
    USER = user
    """Store a message sent by the indicated user in the database"""

    if new == 'yes':
        APP.config['SQLALCHEMY_BINDS'][USER] = f'sqlite:///{USER}.db'
    time = datetime.now()
    DB.create_all()
    data = Message(sender=USER, message=raw_msg, timestamp=time)
    DB.session.add(data)
    DB.session.commit()
