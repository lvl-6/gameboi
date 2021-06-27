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
#from database import Database


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

    pkid = -1  # if it's -1, something is wrong
    discord_id = ''
    steam_id = ''
    games = []
    availability = 0  # should be some sort of Schedule datatype (i.e. 24x7 array list)
    guilds = ['']
    sessions = []

    def __init__(self, pkid):
        # This constructor should take a primary key "id" and use that to pull
        # the player data from the database to populate member vars.
        self.pkid = pkid
        self.get_player_data()

    def get_player_data(self):
        """
        Pull the player data from the database once the pkid is known and set.
        """
        pass