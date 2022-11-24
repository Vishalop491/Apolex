import os, discord,asyncio
from discord.ext import commands
from Data.Devlopers import Devlopers
from Helpers.data import getConfig, updateConfig
import setuptools
from itertools import cycle
import datetime
import aiohttp


proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

class AntiGuild(commands.Cog):
    def __init__(self, client):
        self.client = client                    

    @commands.Cog.listener()
    async def on_guild_update(self, after: discord.Guild,
                              before: discord.Guild) -> None:
       name = before.name
       guild = after    
       data = getConfig(guild.id)
       whitelisted = data["whitelist"]
       async for i in guild.audit_logs(limit=1,
                                            after=datetime.datetime.now() -
                                            datetime.timedelta(minutes=2),
                                            action=discord.AuditLogAction.guild_update):

            if i.user.id in Devlopers:
              return  

            if i.user.id == guild.owner.id:
              return  

            if i.user.id in whitelisted:
              return

            else:
                await guild.ban(i.user,
                                   reason="Apolex | Anti Guild Update")
                await after.edit(name=f"{name}", reason=f"Apolex | Auto Recovery")            

    @commands.Cog.listener()
    async def on_webhook_create(self, channel) -> None:
        guild = channel.guild
        data = getConfig(guild.id)
        whitelisted = data["whitelist"]
        async for i in guild.audit_logs(limit=1,
                                            after=datetime.datetime.now() -
                                            datetime.timedelta(minutes=1),
                                            action=discord.AuditLogAction.webhook_create):

            if i.user.id in Devlopers:
              return  

            if i.user.id == guild.owner.id:
              return

            if i.user.id in whitelisted:
              return

            else:
                await guild.ban(i.user,
                                   reason="Apolex | Anti webhook")
                webhooks = await guild.webhooks()
                for webhook in webhooks:
                    if webhook.id == i.target.id:
                            await webhook.delete()
                            break
                      
    @commands.Cog.listener()
    async def on_webhooks_create(self, channel) -> None:
        guild = channel.guild
        data = getConfig(guild.id)
        whitelisted = data["whitelist"]
        async for i in guild.audit_logs(limit=1,
                                            after=datetime.datetime.now() -
                                            datetime.timedelta(minutes=1),
                                            action=discord.AuditLogAction.webhook_create):

            if i.user.id in Devlopers:
              return  

            if i.user.id == guild.owner.id:
              return

            if i.user.id in whitelisted:
              return

            else:
                await guild.ban(i.user,
                                   reason="Apolex | Anti webhook")
                webhooks = await guild.webhooks()
                for webhook in webhooks:
                    if webhook.id == i.target.id:
                            await webhook.delete()
                            break
                      
    @commands.Cog.listener()
    async def on_webhooks_update(self, channel) -> None:
        guild = channel.guild
        data = getConfig(guild.id)
        whitelisted = data["whitelist"]
        async for i in guild.audit_logs(limit=1,
                                            after=datetime.datetime.now() -
                                            datetime.timedelta(minutes=1),
                                            action=discord.AuditLogAction.webhook_create):

            if i.user.id in Devlopers:
              return  

            if i.user.id == guild.owner.id:
              return

            if i.user.id in whitelisted:
              return

            else:
                await guild.ban(i.user,
                                   reason="Apolex | Anti webhook")
                webhooks = await guild.webhooks()
                for webhook in webhooks:
                    if webhook.id == i.target.id:
                            await webhook.delete()
                            break                    


def setup(client):
	client.add_cog(AntiGuild(client))