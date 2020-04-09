import discord
from discord.ext import commands


class Ban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Ban command
    @commands.command()
    async def ban(self, ctx,member : discord.Member, *, reason=None, delete_message_days=1):
        await member.ban(reason=reason, delete_message_days=delete_message_days)
        await ctx.send(f"Banned {member}")


def setup(bot):
    bot.add_cog(Ban(bot))