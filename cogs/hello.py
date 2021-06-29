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

greeting_msg = ('Hello and welcome to the guild, {0.mention}!\n'
                'Feel free to post anywhere, and if you need verified role '
                'just DM a convener/admin with your student number.\n'
                'To see what commands I have available, mention me and say'
                ' help, like: @gameboi help\n\n'
                '{1.mention} - The general room for general chatter.\n'
                '{2.mention} - Gaming lobby for general game-related chat\n'
                '{3.mention} - Bot command centre for all the bot spam.'
                )

# Configure relevant channel ID's in this dictionary
# Move to another cog one day
channel_ids = {
            'welcome': 123456789,
            'general': 123456789,
            'lobby': 123456789,
            'bot_commands': 123456789,
                }


###############################################################################
# Cog: Hello
###############################################################################

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Greet members as they join"""
        if channel is not None:  # if this fails, try "self.bot.channel" instead.
            room_general = self.bot.get_channel(channel_ids['general'])
            room_lobby = self.bot.get_channel(channel_ids['lobby'])
            room_botcommand = self.bot.get_channel(channel_ids['bot_commands'])
            await channel.send(
                            greeting_msg.format(member, room_general,
                                                room_lobby, room_botcommand)
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
