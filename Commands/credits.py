import discord
from discord.ext import commands


class Credits(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def credits(self, ctx):
        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_author(name="SCROOK | v.1.0 | CREDITS")
        embed.add_field(name="OWNER & DEVELOPER", value="scrook", inline=False)
        embed.add_field(name="WEBSITE", value="scrook.de", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Credits(bot))