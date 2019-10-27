"""Handles the connection to the SQLite database as well as DB interaction"""
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SQLALCHEMY_BINDS'] = { 'we' : 'sqlite:///we.db'}
db = SQLAlchemy(app)

User = ''
class MessageDatabase(db.Model):
    __bind_key__ = User 
    sender = db.Column(db.String(120), primary_key=True, nullable=False)
    message = db.Column(db.String(120), nullable=False)
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return f"MessageDatabase('{self.sender}','{self.message}','{self.timestamp}')"


def store_messages(user, raw_msg, new):
    User = user
    """Store a message sent by the indicated user in the database"""

    if new == 'yes':
        app.config['SQLALCHEMY_BINDS'][User] = f'sqlite:///{User}.db'
    time = datetime.now()
    db.create_all()
    Data = MessageDatabase(sender=User, message=raw_msg, timestamp=time)
    db.session.add(Data)
    db.session.commit()
