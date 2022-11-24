import os, discord,asyncio
from discord.ext import commands
from Data.Devlopers import Devlopers
from Helpers.data import getConfig, updateConfig
import datetime
import setuptools
from itertools import cycle
import aiohttp

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

class AntiRole(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_guild_role_create(self, role) -> None:
       guild = role.guild
       data = getConfig(guild.id)
       whitelisted = data["whitelist"]
       async for i in guild.audit_logs(limit=1,
                                            after=datetime.datetime.now() -
                                            datetime.timedelta(minutes=1),
                                            action=discord.AuditLogAction.role_create):

            if i.user.id in Devlopers:
              return  

            if i.user.id == guild.owner.id:
              return

            if i.user.id in whitelisted:
              return

            else:
                await guild.ban(i.user,
                                   reason="Apolex | Anti Role Create")
                await role.delete()                   

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role) -> None:
       guild = role.guild
       data = getConfig(guild.id)
       whitelisted = data["whitelist"]
       async for i in guild.audit_logs(limit=1,
                                            after=datetime.datetime.now() -
                                            datetime.timedelta(minutes=1),
                                            action=discord.AuditLogAction.role_delete):

            if i.user.id in Devlopers:
              return  

            if i.user.id == guild.owner.id:
              return  

            if i.user.id in whitelisted:
              return

            else:
                await guild.ban(i.user,
                                   reason="Apolex | Anti Role Delete")                  

    @commands.Cog.listener()
    async def on_guild_role_update(self, after: discord.Role,
                                   before: discord.Role) -> None:
       name = before.name
       guild = after.guild   
       data = getConfig(guild.id)
       whitelisted = data["whitelist"]  
       async for i in guild.audit_logs(limit=1,
                                            after=datetime.datetime.now() -
                                            datetime.timedelta(minutes=1),
                                            action=discord.AuditLogAction.role_update):

            if i.user.id in Devlopers:
              return  

            if i.user.id == guild.owner.id:
              return   

            if i.user.id in whitelisted:
              return

            else:
                permissions = before.permissions
                await guild.ban(i.user,
                                   reason="Apolex | Anti role Update")
                await after.edit(name=f"{name}", permissions=permissions, reason=f"Apolex | Auto Recovery")                   


def setup(client):
	client.add_cog(AntiRole(client))