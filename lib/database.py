###############################################################################
# lib/database.py
#
# Author: John C <https://lvl-6.github.io>
# Created: 22/06/2021
#
# Description:
# Contains all relevant database-related methods.
#
###############################################################################

import mariadb # May require rewrite if I end up using another DBMS
import os

###############################################################################
# Configuration Variables
###############################################################################
# TODO: Don't use environment variables here - get them from a file instead.

# Edit these to point it to a different server/database.
# Using environment variables to ensure no passwords accidentally committed.
user = os.getenv('GB_DB_USER')          # User (set up on database)
password = os.getenv('GB_DB_PASSWORD')  # User's password
host = os.getenv('GB_DB_HOST')          # IP address of the database server
port = int(os.getenv('GB_DB_PORT'))     # Port the server is on (default 3306)
database = 'gameboi'                    # The specific database on that server

###############################################################################
# Class: Database
###############################################################################

class Database:
    conn = None # the database connection
    cur = None # the database cursor

    def __init__(self):
        try:
            self.conn = mariadb.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=database
            )
            print(f'Successfully connected to MariaDB platform!')
        except mariadb.Error as e:
            print(f'Error connecting to MariaDB platform: {e}')
        self.cur = self.conn.cursor()

    def test_db(self):
        """Just a test function to make sure all is working, TODO: Delete"""
        self.cur.execute("SELECT id,name FROM test")
        for(id, name) in self.cur:
            print(f'ID: {id}\tNAME: {name}')