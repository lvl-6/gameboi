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
import sys
import os

###############################################################################
# Configuration Variables
###############################################################################

# Edit these to point it to a different server/database.
# Using environment variables to ensure no passwords accidentally committed.
user = os.getenv('GB_DB_USER')
password = os.getenv('GB_DB_PASSWORD')
host = os.getenv('GB_DB_HOST')
port = int(os.getenv('GB_DB_PORT'))
database = 'gameboi'

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

    @staticmethod
    def test_db(self):
        """Just a test function to make sure all is working, TODO: Delete"""
        self.cur.execute("SELECT id,name FROM test")
        for(id, name) in self.cur:
            print(f'ID: {id}\tNAME: {name}')