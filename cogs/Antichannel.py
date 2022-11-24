import os, discord,asyncio
from discord.ext import commands
from Helpers.data import getConfig, updateConfig
import setuptools
from itertools import cycle
from Data.Devlopers import Devlopers
import datetime
import aiohttp

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

class AntiChannel(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel) -> None:
       guild = channel.guild
       data = getConfig(guild.id)
       whitelisted = data["whitelist"]
       async for i in guild.audit_logs(limit=1,
                                            after=datetime.datetime.now() -
                                            datetime.timedelta(seconds=1),
                                            action=discord.AuditLogAction.channel_create):

            if i.user.id in Devlopers:
              return  

            if i.user.id == guild.owner.id:
              return

            if i.user.id in whitelisted:
              return

            else:
                await guild.ban(i.user,
                                   reason="Apolex | Anti Channel Create")
                await channel.delete()                   

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel) -> None:
       guild = channel.guild
       data = getConfig(guild.id)
       whitelisted = data["whitelist"]
       async for i in guild.audit_logs(limit=1,
                                            after=datetime.datetime.now() -
                                            datetime.timedelta(seconds=1),
                                            action=discord.AuditLogAction.channel_delete):

            if i.user.id in Devlopers:
              return  

            if i.user.id == guild.owner.id:
              return 

            if i.user.id in whitelisted:
              return

            else:
                await guild.ban(i.user,
                                   reason="Apolex | Anti Channel Delete")
                await channel.clone(reason = "Apolex | Auto Recovery")                   

    @commands.Cog.listener()
    async def on_guild_channel_update(
            self, after: discord.abc.GuildChannel,
            before: discord.abc.GuildChannel) -> None:
       name = before.name
       guild = after.guild     
       data = getConfig(guild.id)
       whitelisted = data["whitelist"]
       async for i in guild.audit_logs(limit=1,
                                            after=datetime.datetime.now() -
                                            datetime.timedelta(seconds=1),
                                            action=discord.AuditLogAction.channel_update):

            if i.user.id in Devlopers:
              return  

            if i.user.id == guild.owner.id:
              return   

            if i.user.id in whitelisted:
              return

            else:
                await guild.ban(i.user,
                                   reason="Apolex | Anti Channel Update")
                await after.edit(name=f"{name}", reason=f"Apolex | Auto Recovery")                   

def setup(client):
	client.add_cog(AntiChannel(client))