# LFG Bot "Gameboi"

## About this project
This is my (WIP) LFG bot which I had originally started writing for my college's E-Sports society but now it's my
pet project. It supports player accounts (in which you can link your profiles and list your games), and organises
gaming sessions into a Session object to which players can mark their interest (or "RSVP").

### Classes:
#### Player
  Holds information about the player i.e. Name, Discord ID, Steam ID, list of games, Session RSVP, availability, etc.
#### Session
  Holds information about a specific gaming session i.e. game, time, parameters, players involved, etc.
#### GameList
  Holds a list of Games and methods for manipulating and searching that list i.e. addGame().
  An instance will be held by Players and Events.
#### Game
  Holds information about a game i.e. name, icon, links (dict), etc.
#### Event
  Holds information about an Event (like a tournament) i.e. Session instance(s), prize, bracket, etc.

## Dependencies
Use the following command to install all dependencies of this project:
```
pip install discord mariadb
```
If I've missed anything, just read the errors, it will be pretty obvious.

## Other requirements
This project uses a MariaDB (MySQL) database. Go here for info about the schema: [The Database](https://github.com/lvl-6/gameboi/wiki/The-Database)
For testing, I recommend you launch a VM with RHEL/CentOS (or your preferred distro) and set up MariaDB on that.

## Further notes
Shrek is coming to get you