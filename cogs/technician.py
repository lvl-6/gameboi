###############################################################################
# cogs/technician.py
#
# Author: John C <https://lvl-6.github.io>
# Created: 31/01/2021
#
# Description:
# A bunch of functions for our glorious bot technicians to control the bot,
# and set it right when things go wrong.
#
###############################################################################

import discord
from discord.ext import commands

technician_role = 'Bot Technician' # Probably should not be in this scope


###############################################################################
# Cog: Technician
###############################################################################

class Technician(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.has_role(technician_role)
    @commands.command()
    async def list_cogs(self, ctx, *, args):
        """List the cogs available to this bot"""
        #member = member or ctx.author
        await ctx.send('Command not yet implemented.')

    @commands.has_role(technician_role)
    @commands.command()
    async def reload(self, ctx, extension):
        """
        Reload a cog by passing its name after the command (quotes work btw)
        """
        #member = ctx.author
        message = ctx.message.content
        await ctx.send('Reloading cog: ' + extension)
        self.bot.reload_extension('cogs.' + extension) # Should call this from root module (gb.py) but fuck me easier said than done
        #gb.reload_extension(extension)
        await ctx.send('It should be reloaded now (checks not implemented).')


###############################################################################
# Setup
###############################################################################

def setup(bot):
    bot.add_cog(Technician(bot))
