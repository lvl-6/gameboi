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
import configparser

###############################################################################
# Configuration Variables
###############################################################################

config = configparser.ConfigParser()
config.read('settings.cfg') # settings.cfg in the project root (next to gb.py)
config = config['DATABASE']

# Edit these to point it to a different server/database.
user = config['User']           # User (set up on database)
password = config['Password']   # User's password
host = config['Host']           # IP address of the database server
port = int(config['Port'])      # Port the server is on (default 3306)
database = 'gameboi'            # The specific database on that server


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
