###############################################################################
# lib/session.py
#
# Author: John C <https://lvl-6.github.io>
# Created: 02/06/2021
# 
# Description:
# Contains the class Session, which holds information about a planned gaming
# session, including a list of Players who will be present.
# 
###############################################################################

import lib.database
import lib.player
import mariadb
import datetime
from enum import Enum

db = lib.database.db


# An enum to hold RSVP status
class Rsvp(Enum):
    NO = 0
    YES = 1
    MAYBE = 2


###############################################################################
# Class: Session
###############################################################################

class Session:
    """
    Holds information about a planned gaming session.

    Variables:
        pkid (int): The primary key from the database which refers to this session.
        game (Game): The game which players will be playing.
        date (date): The date on which this session takes place. Format: YYYY-MM-DD
        time (time): The time at which this session takes place. Format: HH:MM:SS
        options (List<str>):  Any interesting game options (i.e. FFA, 3v3, hardmode).
        players (dict): Holds Player objects as the keys, and RSVP status as the values.
        server (str): The IP address of the server (if any), or None.
    """

    pkid = None
    game = None
    date = None  # Format: YYYY-MM-DD
    time = None  # Format: HH:MM:SS
    options = []
    players = {}
    server = ''

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

    def get_session_data(self):
        """
        Pull the basic session data from the database once the pkid is known and set.
        """
        if self.pkid is None:
            raise Exception("self.pkid is None - set it before calling this function!")

        db.open()
        try:
            db.cur.execute("SELECT gameid,datetime,server FROM sessions WHERE id=%s", (self.pkid,))
            for(gameid, datetime, server) in db.cur:
                # Debug print
                print(
                    "Pulled session data...\n"
                    "ID:\t\t" + str(self.pkid) + "\n"
                    + "GameID:\t\t" + str(gameid) + "\n"
                    + "Date / Time:\t" + str(datetime) + "\n"
                    + "Server:\t\t" + server
                )
                # Set the values
                self.game = None  # TODO: Get game from table "games" by gameid here.
                # Yep it's also called "datetime" in the db... not to be confused with the datetime module. Woops.
                self.date = datetime.date()  # This is our "datetime" object from the db...
                self.time = datetime.time()  # Same...
                self.server = server
        except mariadb.Error as e:
            print(f"SQL error receiving session details from database: {e}")
        db.close()

    def get_options(self):
        """
        Get the relevant options for this session (i.e. gamemode, map, team size, params, etc)
        """
        self.options.clear()
        db.open()
        try:
            db.cur.execute("SELECT option FROM session_options WHERE sessionid=%s", (self.pkid,))
            for (option) in db.cur:
                # Debug print
                print(
                    "Pulled session options data...\n"
                    + "ID:\t\t" + str(self.pkid) + "\n"
                    + "Option:\t\t" + option[0]  # Index required because option is given as a single-item tuple.
                )
                # Add each option to the options list
                self.options.append(option[0])
        except mariadb.Error as e:
            print(f"SQL error receiving session details from database: {e}")
        db.close()

    def get_players(self):
        """
        Get the Players who have RSVP'd this Session.
        """
        self.players.clear()  # Clear this in case for some reason pkid was changed instead of creating a new Session.
        db.open()
        try:
            db.cur.execute(
                "SELECT session_players.playerid, session_players.rsvp, "
                "players.name, players.discordid, players.steamid64 "
                "FROM session_players INNER JOIN players "
                "ON session_players.playerid=players.id WHERE session_players.sessionid=%s", (self.pkid,)
            )
            for (playerid, rsvp, name, discordid, steamid64) in db.cur:
                rsvp = lib.session.Rsvp(rsvp)
                # Debug print
                print(
                    "Pulled player data...\n"
                    "SessionID:\t" + str(self.pkid) + "\n"
                    + "PlayerID:\t" + str(playerid) + "\n"
                    + "Name:\t\t" + name + "\n"
                    + "RSVP:\t\t" + rsvp.name + "\n"
                    + "DiscordID:\t" + discordid + "\n"
                    + "SteamID64:\t" + steamid64
                )
                # If this player has given any RSVP except NO, it's time to do the things...
                if rsvp == Rsvp.YES or rsvp == Rsvp.MAYBE:
                    # Create the Player object
                    current_player = lib.player.Player()
                    current_player.pkid = playerid
                    current_player.name = name
                    current_player.discord_id = discordid
                    current_player.steam_id = steamid64
                    # Add to the dict
                    self.players[current_player] = rsvp
        except mariadb.Error as e:
            print(f"SQL error receiving player details from database: {e}")
        db.close()

    def __hash__(self):
        return hash(self.pkid)  # Yes this just returns the pkid... do I even need to hash? Dunno.

    def __eq__(self, other):
        return self.pkid == other  # we're only comparing by pkid because it should be unique anyway.

    def __ne__(self, other):
        # To avoid having both x==y and x!=y
        # true at the same time
        return not (self == other)
