import discord
from datetime import datetime
from discord.ext import commands


class Ready(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Ready event
    @commands.Cog.listener()
    async def on_ready(self):
        nowdate = datetime.now()
        localdate = nowdate.strftime("%d/%m/%y")
        localtime = nowdate.strftime("%H:%M:%S")
        print(f"Scrookbot is online! \nDate: {localdate} \nTime: {localtime}")


def setup(bot):
    bot.add_cog(Ready(bot))