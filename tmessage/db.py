"""Handles the connection to the SQLite database as well as DB interaction"""
from datetime import datetime

from peewee import CharField, DateTimeField, Model, SqliteDatabase


def database(user, raw_msg, new):
    """user for sender, raw_msg for message, new if the user is new"""
    MESSAGES_DB = SqliteDatabase(f'{user}.db')# pylint: disable=invalid-name


    class Message(Model):
        """Message table - keeps track of message sent and received"""
        sender = CharField()
        message = CharField()
        timestamp = DateTimeField()

        class Meta:  # pylint: disable=missing-class-docstring,too-few-public-methods
            database = MESSAGES_DB


    if new == True: # pylint: disable=singleton-comparison
        MESSAGES_DB.create_tables([Message])
    time = datetime.now()
    Message.create(sender=user, message=raw_msg, timestamp=time)
