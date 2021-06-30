###############################################################################
# lib/game.py
#
# Author: John C <https://lvl-6.github.io>
# Created: 02/06/2021
# 
# Description:
# Contains the classes Game and GameList, which hold information about games
# and lists of Games, respectively.
# 
###############################################################################

import lib.database
import mariadb

db = lib.database.db


###############################################################################
# Class: Game
###############################################################################

class Game:
    """
    Holds information about an individual game.

    Variables:
        pkid (int): The primary key from the database which refers to this game.
        name (str): The name of the game.
        icon (str): The path to the game's icon.
        links (dict): Relevant links i.e. Steam page. Key: name of link, value: link.
    """

    pkid = None
    name = ''
    icon = ''
    links = {}

    def __init__(self):
        """
        Constructor.
        """
        pass

    def set_pkid(self, pkid):
        """
        Simple little setter for pkid.
        @param pkid: the id we want to set self.pkid to.
        @return: None.
        """
        self.pkid = pkid

    def get_game_data(self):
        """
        Pull the basic game data from the database once the pkid is known and set.
        """
        if self.pkid is None:
            raise Exception("self.pkid is None - set it before calling this function!")

        db.open()
        try:
            db.cur.execute("SELECT name,icon FROM games WHERE id=%s", (self.pkid,))
            for(name, icon) in db.cur:
                # Debug print
                print(
                    "Pulled game data...\n"
                    "ID:\t\t" + str(self.pkid) + "\n"
                    + "Name:\t\t" + name + "\n"
                    + "Icon Path:\t" + icon
                )
                # Set the values
                self.name = name
                self.icon = icon
        except mariadb.Error as e:
            print(f"SQL error receiving game details from database: {e}")
        db.close()


###############################################################################
# Class: GameList
###############################################################################

class GameList:
    """
    Holds a list of games owned by a player or played at an event.
    Yep it's kind of unnecessary but I designed it this way... may remove later.

    Variables:
        games (list): List of Game objects
    """

    list = []

    def __init__(self):
        """
        Constructor
        """
        pass
