import discord
import os
import secrettoken
from discord.ext import commands


bot = commands.Bot(command_prefix= "+")
bot.remove_command("help")

for filename in os.listdir("./Commands"):
    if filename.endswith(".py"):
        bot.load_extension(f"Commands.{filename[:-3]}")


bot.run(secrettoken.tkn)
