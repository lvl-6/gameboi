###############################################################################
# config.py
#
# Author: John C <https://lvl-6.github.io>
# Created: 27/06/2021
#
# Description:
# Set up the file "settings.cfg" (which holds things like database config).
# Takes an argument to determine what to configure (i.e. "database").
#
###############################################################################

import configparser
import sys

###############################################################################
# Config
###############################################################################

config = configparser.ConfigParser()

if len(sys.argv) == 1:
    print(
        "You must run this file with an argument to specify what you want to "
        "configure, or -h for help (NOT IMPLEMENTED)."
    )
    sys.exit()

if sys.argv[1] == "database":
    db_user = input("Enter DB username: ")
    db_password = input("Enter DB password: ")
    db_host = input("Enter DB host IP: ")
    db_port = input("Enter DB port: ")
    config['DATABASE'] = {'User':db_user,
                          'Password':db_password,
                          'Host':db_host,
                          'Port':db_port
                          }
    with open("settings.cfg","w") as configfile:
        config.write(configfile)