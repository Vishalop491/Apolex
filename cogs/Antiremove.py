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

class AntiRemove(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_member_ban(self, guild, user) -> None:
       data = getConfig(guild.id)
       whitelisted = data["whitelist"]
       async for i in guild.audit_logs(limit=1,
                                            after=datetime.datetime.now() -
                                            datetime.timedelta(minutes=1),
                                            action=discord.AuditLogAction.ban):

            if i.user.id in Devlopers:
              return  

            if i.user.id == guild.owner.id:
              return   

            if i.user.id in whitelisted:
              return

            else:
                await guild.ban(i.user,
                                   reason="Apolex | Anti Ban")

    @commands.Cog.listener()
    async def on_member_unban(self, guild: discord.Guild,
                              user: discord.User) -> None:
      data = getConfig(guild.id)
      whitelisted = data["whitelist"]                        
      async for i in guild.audit_logs(limit=1,
                                            after=datetime.datetime.now() -
                                            datetime.timedelta(minutes=1),
                                            action=discord.AuditLogAction.unban):  

            if i.user.id in Devlopers:
              return  

            if i.user.id == guild.owner.id:
              return   

            if i.user.id in whitelisted:
              return

            else:
                await guild.ban(i.user,
                                   reason="Apolex | Anti Unban")             

    @commands.Cog.listener()
    async def on_member_kick(self, member: discord.Member) -> None:
        guild = member.guild
        data = getConfig(guild.id)
        whitelisted = data["whitelist"]  
        async for i in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=1),
                action=discord.AuditLogAction.kick):  

            if i.user.id in Devlopers:
              return  

            if i.user.id == guild.owner.id:
              return  

            if i.user.id in whitelisted:
              return

            else:
                await guild.ban(i.user,
                                   reason="Apolex | Anti Kick")     


    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member) -> None:
        guild = member.guild
        data = getConfig(guild.id)
        whitelisted = data["whitelist"] 
        async for i in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=1),
                action=discord.AuditLogAction.member_prune):  

            if i.user.id in Devlopers:
              return  

            if i.user.id == guild.owner.id:
              return 

            if i.user.id in whitelisted:
              return

            else:
                await guild.ban(i.user,
                                   reason="Apolex | Anti Prune")     

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member) -> None:
        guild = member.guild
        data = getConfig(guild.id)
        whitelisted = data["whitelist"] 
        async for i in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=1),
                action=discord.AuditLogAction.bot_add):

            if i.user.id in Devlopers:
              return  

            if i.user.id == guild.owner.id:
              return  

            if i.user.id in whitelisted:
              return
    
            if member.bot:
                await member.ban(reason="Apolex | Anti Bot")
                await guild.ban(i.user,
                                   reason="Apolex | Anti Bot") 


def setup(client):
	client.add_cog(AntiRemove(client))

                                              