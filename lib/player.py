###############################################################################
# lib/player.py
#
# Author: John C <https://lvl-6.github.io>
# Created: 02/06/2021
# 
# Description:
# Contains the class Player, which holds information about an individual
# player.
# 
###############################################################################

from lib.game import Game, GameList
from lib.session import Session
import lib.database
import mariadb

db = lib.database.db


###############################################################################
# Class: Player
###############################################################################

class Player:
    """
    Holds information about an individual player.

    Variables:
        pkid (int): The primary key from the database which refers to this
player.
        discord_id (str): The player's Discord ID.
        steam_id (str): The player's Steam ID (optional).
        games (GameList): List of games owned by the player.
        availability (Schedule): Times/days the player plans to be available.
        guilds (List<str>): List of guilds in which this player is a member
and is registered with the bot.
        sessions (List<Session>): List of Sessions this player has RSVPed.
    """

    pkid = None
    name = ''
    discord_id = ''
    steam_id = ''
    games = []
    availability = 0  # TODO: NOT YET IMPLEMENTED! Should be some sort of Schedule datatype (i.e. 24x7 array list)
    guilds = ['']  # TODO: NOT YET IMPLEMENTED! Create new table "player_guilds" in db with compound key but only 1 FK.
    sessions = []

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

    def get_player_data(self):
        """
        Pull the basic player data from the database once the pkid is known and set.
        """
        if self.pkid is None:
            raise Exception("self.pkid is None - set it before calling this function!")

        db.open()
        try:
            db.cur.execute("SELECT name,discordid,steamid64 FROM players WHERE id=%s", (self.pkid,))
            for(name, discordid, steamid64) in db.cur:
                # Debug print
                print(
                    "Pulled player data...\n"
                    "ID:\t\t" + str(self.pkid) + "\n"
                    + "Name:\t\t" + name + "\n"
                    + "Discord ID:\t" + discordid + "\n"
                    + "SteamID64:\t" + steamid64
                )
                # Set the values
                self.name = name
                self.discord_id = discordid
                self.steam_id = steamid64
        except mariadb.Error as e:
            print(f"SQL error receiving player details from database: {e}")
        db.close()
