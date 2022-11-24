import discord
import logging
from discord.ext import commands
import motor.motor_asyncio as mongodb
from itertools import cycle

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

class ready(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.color = 0x2f3136
        self.connection = mongodb.AsyncIOMotorClient("mongodb+srv://hacker:chetan2004@cluster0.rxh8r.mongodb.net/Flame?retryWrites=true&w=majority")
        self.db = self.connection["Zeon"]["servers"]

    @commands.Cog.listener()
    async def on_ready(self):
        for server in self.client.guilds:
            data = await self.db.find_one({"guild": server.id})
            if data == None:
                await self.db.insert_one(
                    {
                        "guild": server.id,
                        "log-channel": None,
                        "delete-after" : None,
                        "joinvc": {
                            "channelid": None,
                            "enabled": False
                        },
                        "vcrole": {
                            "roleid": None,
                            "enabled": False
                        },
                        "autorole": [],
                        "humans": [],
                        "bots": [],
                        "welcome": {
                            "message": None,
                            "channel": None,
                            "enabled": False,
                            "embed": False,
                            "title": None,
                            "description": None,
                            "thumbnail": None,
                            "image": None
                        }
                    }
                )

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await self.db.insert_one(
            {
                "guild": guild.id,
                "log-channel": None, 
                "delete-after" : None,
                "joinvc": {
                    "channelid": None,
                    "enabled": False
                },
                "vcrole": {
                    "roleid": None,
                    "enabled": False
                },
                "autorole": [],
                "humans": [],
                "bots": [],
                "welcome": {
                    "message": None,
                    "channel": None,
                    "enabled": False,
                    "embed": False,
                    "title": None,
                    "description": None,
                    "thumbnail": None,
                    "image": None
                }
            }
        )

    @commands.Cog.listener()
    async def on_shard_ready(self, shard_id):
        logging.info("Shard #%s is ready" % (shard_id))

    @commands.Cog.listener()
    async def on_shard_connect(self, shard_id):
        logging.info("Shard #%s has connected" % (shard_id))

    @commands.Cog.listener()
    async def on_shard_disconnect(self, shard_id):
        logging.info("Shard #%s has disconnected" % (shard_id))

    @commands.Cog.listener()
    async def on_shard_resume(self, shard_id):
        logging.info("Shard #%s has resumed" % (shard_id))

def setup(client):
    client.add_cog(ready(client))