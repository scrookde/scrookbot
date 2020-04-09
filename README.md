# SCROOKBOT

Scrookbot is a Discordbot which is using the discord.py API

## Installation

Use package manager [pip](https://pip.pypa.io/en/stable/) to install discord.py.

```bash
pip install discord.py
```

## Usage

```python
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
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
