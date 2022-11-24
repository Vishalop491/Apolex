import os, discord,asyncio
from discord.ext import commands
from Helpers.data import getConfig, updateConfig
from Data.Devlopers import Devlopers
import json
import datetime
from itertools import cycle

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}


class Logs(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        data = getConfig(guild.id)
        updateConfig(guild.id, data)

        bot_entry = await guild.audit_logs(action=discord.AuditLogAction.bot_add).flatten()
        try:
          join = discord.Embed(title="**Thank You For choosing Apolex!**",
                             description=f"""
**Features?**

• AntiNuke
• Moderation
• Join To Create
• Globalchat
• Music
• Giveaway
• AutoMod
• Welcome, And Much More""")
          await bot_entry[0].user.send(embed=join)
        except discord.errors.Forbidden:
          pass

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
      with open("config.json", "r") as f:
          data = json.load(f)

      del data["guilds"][str(guild.id)]

      with open("config.json", "w") as f:
          json.dump(data, f)             


def setup(client):
	client.add_cog(Logs(client))