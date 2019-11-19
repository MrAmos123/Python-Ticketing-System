import sqlite3
import os
import random
import string

class Database:
    def __init__(self):
        self.db_tid = 0
        self.db_connection = None

        # create db if doesn't exist.
        if os.path.exists('database.db'):
            self.db_connection = sqlite3.connect('database.db')
            self.db_cursor = self.db_connection.cursor()
        else:
            self.db_connection = sqlite3.connect('database.db')
            self.db_cursor = self.db_connection.cursor()
            self.db_cursor.execute('CREATE TABLE tickets (tid INTEGER PRIMARY KEY AUTOINCREMENT, \
                                    ticketid TEXT NOT NULL, raisedby TEXT NOT NULL, assignedto TEXT NOT NULL, description TEXT NOT NULL)')
            self.db_connection.commit()

    def ent_data(self, user_raisedby, user_shortdesc):
        # Placeholder
        user_assignedto = 'Jeff'
        self.db_cursor.execute('SELECT * FROM tickets ORDER BY tid DESC LIMIT 1')
        # insert new data
        self.db_cursor.execute('INSERT INTO tickets (raisedby, description, assignedto) VALUES(?, ?, ?)',
                               (user_raisedby if len(user_raisedby) > 0 else None,
                                user_shortdesc if len(user_shortdesc) > 0 else None, user_assignedto))

    def close_cursor(self):
        self.db_connection.commit()
        self.db_cursor.close()
