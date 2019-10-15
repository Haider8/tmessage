"""Handles the connection to the SQLite database as well as DB interaction"""
from datetime import datetime

from peewee import CharField, DateTimeField, Model, SqliteDatabase


MESSAGES_DB = SqliteDatabase('message_store.sqlite')


class Message(Model):
    """Message table - keeps track of message sent and received"""
    sender = CharField()
    message = CharField()
    timestamp = DateTimeField()

    class Meta:  # pylint: disable=missing-class-docstring,too-few-public-methods
        database = MESSAGES_DB

@MESSAGES_DB
def grab_messages(user):
    """Grab messages from the user"""
    cursor = MESSAGES_DB.execute_sql(
            "SELECT sender, message FROM message where sender LIKE \'"+ user +'\'')
    return [r for r in cursor.fetchall()]
    
@MESSAGES_DB
def store_messages(user, raw_msg):
    """Store a message sent by the indicated user in the database"""
    time = datetime.now()
    Message.create(sender=user, message=raw_msg, timestamp=time)


MESSAGES_DB.create_tables([Message])
