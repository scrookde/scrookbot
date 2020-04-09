import discord
from discord.ext import commands


class Kick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Kick command
    @commands.command()
    async def kick(self, ctx,member : discord.Member,):
        await member.kick()
        await ctx.send(f"Kicked {member}")


def setup(bot):
  bot.add_cog(Kick(bot))