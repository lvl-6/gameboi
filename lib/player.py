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
        name (str): The player's preferred name.
        discord_id (str): The player's Discord ID.
        steam_id (str): The player's Steam ID (optional).
        games (GameList): List of games owned by the player.
        availability (Schedule): Times/days the player plans to be available.
        guilds (List<str>): List of guilds in which this player is a member
and is registered with the bot.
        sessions (dict): List of Sessions this player has RSVPed. Dict Key: Session, Value: RSVP.
    """

    pkid = None
    name = ''
    discord_id = ''
    steam_id = ''
    games = GameList()
    availability = 0  # TODO: NOT YET IMPLEMENTED! Should be some sort of Schedule datatype (i.e. 24x7 array list)
    guilds = ['']  # TODO: NOT YET IMPLEMENTED! Create new table "player_guilds" in db with compound key but only 1 FK.
    sessions = {}  # Key: Session, Value: RSVP.

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

    def get_owned_games(self):
        """
        Get all the games owned by this player and put them into games list.
        """
        self.games.list.clear()  # Clear this first in case this isn't the first time it was called
        db.open()
        try:
            # Join data from games table to player_games bridge table
            db.cur.execute(
                "SELECT player_games.gameid,"
                "games.name, games.icon "
                "FROM player_games INNER JOIN games "
                "ON player_games.gameid=games.id WHERE playerid=%s", (self.pkid,)
            )
            for(gameid, name, icon) in db.cur:
                # Debug print
                print(
                    "Pulled game data...\n"
                    "PlayerID:\t" + str(self.pkid) + "\n"
                    + "GameID:\t\t" + str(gameid) + "\n"
                    + "Name:\t\t" + name + "\n"
                    + "Icon Path:\t" + icon
                )
                # Create Game object
                current_game = lib.game.Game()
                current_game.pkid = gameid
                current_game.name = name
                current_game.icon = icon
                # Add game to list of owned games
                self.games.list.append(current_game)
        except mariadb.Error as e:
            print(f"SQL error receiving player-owned games from database: {e}")
        db.close()

    def get_sessions(self):
        """
        Get all the Sessions that this Player has responded to and put them into sessions list.
        """
        self.sessions.clear()  # Clear this first in case this isn't the first time it was called
        db.open()
        try:
            # Join data from sessions table to session_players bridge table
            db.cur.execute(
                "SELECT session_players.sessionid,"
                "session_players.rsvp, sessions.gameid,"
                "sessions.datetime, sessions.server "
                "FROM session_players INNER JOIN sessions "
                "ON session_players.sessionid=sessions.id WHERE playerid=%s", (self.pkid,)
            )
            for(sessionid, rsvp, gameid, datetime, server) in db.cur:
                # Debug print
                print(
                    "Pulled session data...\n"
                    "PlayerID:\t" + str(self.pkid) + "\n"
                    + "SessionID:\t" + str(sessionid) + "\n"
                    + "GameID:\t\t" + str(gameid) + "\n"
                    + "RSVP:\t\t" + str(rsvp) + "\n"
                    + "Date / Time:\t" + str(datetime) + "\n"
                    + "Server:\t\t" + server
                )
                # Create Session & Game objects
                current_session = lib.session.Session()
                current_session.pkid = sessionid
                current_game = lib.game.Game()
                current_game.pkid = gameid
                current_game.get_game_data()
                current_session.game = current_game
                # TODO: convert rsvp to an enum or something for readability
                current_session.date = datetime.date()  # This is our "datetime" object from the db...
                current_session.time = datetime.time()  # Same...
                current_session.server = server
                # Add session to dict of RSVP'd Sessions
                self.sessions[current_session] = rsvp
        except mariadb.Error as e:
            print(f"SQL error receiving player-owned games from database: {e}")
        # Don't need to close apparently because get_game_data() already closed it... TODO: Investigate.
