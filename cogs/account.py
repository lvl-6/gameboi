###############################################################################
# cogs/account.py
#
# Author: John C <https://lvl-6.github.io>
# Created: 31/05/2021
#
# Description:
# Handles Player accounts for the bot.
#
###############################################################################

import discord
from discord.ext import commands

# TODO: Temporary! Accounts should be stored as Players in a proper database.
member_id_list = ['']


###############################################################################
# Cog: Account
###############################################################################

class Account(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def register(self, ctx):
        """Register an account with the bot"""
        member = ctx.author
        """ TODO: Delete this, old code.
        if not Account.accountExists(str(member.id)):
            Account.create_account(member)
            await ctx.send(
                    'Account created successfully for {0.id}.\n'
                    'Welcome to the club!\n'.format(member)
            )
        else:
            await ctx.send(
                    'An account already exists for {0.id}'.format(member)
            )
        """

    @staticmethod
    def create_account(member: discord.Member = None):
        """Create a Player account for a given member"""
        # TODO: Should utilise Player class once implemented!
        global member_id_list
        if member is None:
            # Temporary error return (should probably throw a proper exception).
            return 'Error! No discord.Member was passed to createAccount().'
        else:
            member_id_list.append(str(member.id))
            return 'Account created successfully for {0.id}!'.format(member)

    def accountExists(member_id: str):
        """Check if a player account exists"""
        if member_id in member_id_list:
            return True
        else:
            return False


###############################################################################
# Setup
###############################################################################

def setup(bot):
    bot.add_cog(Account(bot))
