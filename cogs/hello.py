###############################################################################
# (Ripped from a previous bot, just a placeholder cog for reference purposes.)
# cogs/hello.py
#
# Author: John C <https://lvl-6.github.io>
# Created: 28/09/2020
#
# Description:
# An example cog which greets users both on join, and on command.
#
###############################################################################

import discord
from discord.ext import commands


###############################################################################
# Cog: Hello
###############################################################################

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Greet members as they join"""
        if channel is not None:
            await channel.send(
                    'Hello and welcome to the guild, {0.mention}!\n'
                    'Feel free to post anywhere, and if you need verified\n'
                    'role just DM a convener/admin with your student number.'
                    .format(member)
                    )

    @commands.command()
    async def hello_there(self, ctx, *, member: discord.Member = None):
        """Says the thing"""
        member = member or ctx.author
        await ctx.send(
                'General {0.mention}.'.format(member)
                )


###############################################################################
# Setup
###############################################################################

def setup(bot):
    bot.add_cog(Hello(bot))