"""Handles the connection to the SQLite database as well as DB interaction"""
from datetime import datetime
import sqlite3


CONNECTION = sqlite3.connect('message_store.sqlite')
CONNECTION.row_factory = sqlite3.Row

with CONNECTION:
    # Sets up the table we use to store all messages
    CONNECTION.execute(
        'CREATE TABLE IF NOT EXISTS messages ('
        'id INTEGER PRIMARY KEY,'
        'sender TEXT NOT NULL,'
        'message TEXT NOT NULL,'
        'sent_at TIMESTAMP NOT NULL'
        ');'
    )


def store_messages(user, raw_msg):
    """Store a message sent by the indicated user in the database"""
    time = datetime.now()

    with CONNECTION:
        CONNECTION.execute(
            'INSERT INTO messages (sender, message, sent_at) VALUES (?, ?, ?)',
            (user, raw_msg, time),
        )
