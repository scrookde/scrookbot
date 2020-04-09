import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    # Help command
    @commands.command()
    async def help(self, ctx):

        embed = discord.Embed(colour= discord.Colour.blue())
        embed.set_author(name="SCROOK | v.1.0 | HELP")
        embed.add_field(name="HELP", value="+help | Returns that what you see know!", inline=False)
        embed.add_field(name= "PING", value= "+ping | Returns Pong!", inline=False)
        embed.add_field(name="BAN", value="+ban [user] [reason] [delete_messages_days]", inline=False)
        embed.add_field(name="UNBAN", value="+unban [user]", inline=False)
        embed.add_field(name="KICK", value="+kick [user]", inline=False)
        embed.add_field(name="CLEAR", value="+clear [amount of messages]", inline=False)
        embed.add_field(name="CREDITS", value="+credits | Returns Credit list.]", inline=False)
        embed.set_footer(text="scrookbot | by scrook | website: scrookbot.de")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
