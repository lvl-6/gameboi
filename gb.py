###############################################################################
# gameboi
# ./gb.py
#
# Author: John C <https://lvl-6.github.io>
# Created: 31/01/2021
#
# Description:
# A bot for game stuff, made for CitySA E-Sports Society.
#
###############################################################################

import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot as BotBase
from lib.database import Database

import lib.logging as logging

version = '0.0.1'
bot_token = os.getenv('GBOI_TOKEN')


###############################################################################
# Bot Initialisation
###############################################################################

# We will load only the cogs in this list for security reasons.
extensions = ['cogs.hello', 'cogs.technician', 'cogs.account']  # TODO

bot = BotBase(
    command_prefix=commands.when_mentioned,
    description='I do game stuff.',
    owner_ids=0,
    case_insensitive=True,
    )

# Program is running as main (i.e. not imported by another program)
if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)
        logging.print_log('Loaded extension: ' + extension)


# This doesn't get called from the Technician cog btw!
async def reload_extension(extension: str, ctx):
    logging.print_log('Received command to reload extension: ')
    bot.reload_extension('cogs.'+extension)


@bot.event
async def on_connect():
    logging.print_log('Bot has connected to Discord.')


@bot.event
async def on_disconnect():
    logging.print_log('Bot has disconnected from Discord.')


@bot.event
async def on_ready():
    logging.print_log('Bot is ONLINE and READY.')


###############################################################################
# Program Execution
###############################################################################

bot.run(bot_token)
