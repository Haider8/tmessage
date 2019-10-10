from datetime import datetime
import sqlite3


connection = sqlite3.connect('message_store.sqlite')
connection.row_factory = sqlite3.Row

with connection:
    # Sets up the table we use to store all messages
    connection.execute(
        'CREATE TABLE IF NOT EXISTS messages ('
        'id INTEGER PRIMARY KEY,'
        'sender TEXT NOT NULL,'
        'message TEXT NOT NULL,'
        'sent_at TIMESTAMP NOT NULL'
        ');'
    )


def store_messages(user, raw_msg):
    time = datetime.now()

    with connection:
        connection.execute(
            'INSERT INTO messages (sender, message, sent_at) VALUES (?, ?, ?)',
            (user, raw_msg, time),
        )
