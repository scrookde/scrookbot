import discord
from discord.ext import commands
import os
from pythonping import ping

class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Ping command
    @commands.command()
    async def ping(self, ctx):
        if (len(ctx.message.content.split(" ")) == 1):
            await ctx.send("Pong!") #wait until send..
            return
        else:
            address = ctx.message.content.split(" ")[1]
            await self.pingServer(ctx, address)

    async def pingServer(self, ctx, address):
        await ctx.send("Going to Ping: " + address)
        try:
            res = ping(address, count=1)
            if (res.success):
                await ctx.send("Ping Successful in: " +str(res.rtt_avg_ms)+ "ms")
            else:
                await ctx.send("Host was unreachable.")
        except Exception as ex:
            print(ex)
            await ctx.send("Error, is the Hostname valid?")

def setup(bot):
    bot.add_cog(Ping(bot))