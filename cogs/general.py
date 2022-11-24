import time
import discord
import logging
import requests
from discord.ext import commands
import motor.motor_asyncio as mongodb
from discord.colour import Color
from itertools import cycle

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

logging.basicConfig(
    level=logging.INFO,
    format=
    "\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)


class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = discord.Colour.green()
        self.connection = mongodb.AsyncIOMotorClient(
            "mongodb+srv://hacker:chetan2004@secure.9rv0s.mongodb.net/secure?retryWrites=true&w=majority"
        )
        self.db = self.connection["secure"]["servers"]


      
    @commands.group(name="status",
                      description="Shows users status",
                      usage="status <member>")
    async def status(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        status = member.status
        if status == discord.Status.offline:
            status_location = "Not Applicable"
        elif member.mobile_status != discord.Status.offline:
            status_location = "Mobile"
        elif member.web_status != discord.Status.offline:
            status_location = "Browser"
        elif member.desktop_status != discord.Status.offline:
            status_location = "Desktop"
        else:
            status_location = "Not Applicable"
        await ctx.send(embed=discord.Embed(title="<:sowlbz:989006711920668703> | Status",
                                           description="`%s`: `%s`" %
                                           (status_location, status),
                                           color=0x2f3136))

    @commands.group(name="boosts",
                      description="Shows boosts count",
                      usage="boosts",
                      aliases=["bc"])
    async def boosts(self, ctx):
        await ctx.send(
            embed=discord.Embed(title="<:sowlbz:989006711920668703> boosts",
                                description="**`%s`**" %
                                (ctx.guild.premium_subscription_count),
                                color=0x2f3136))

    @commands.group(name="emonznzji-add",
                      description="Addnsnxs a emoji",
                      usage="emozjzjzji-add [emoji]",
                      aliases=["addddd"])
    @commands.has_permissions(manage_emojis=True)
    async def steansjsnzl(self, ctx, emote):
        try:
            if emote[0] == '<':
                name = emote.split(':')[1]
                emoji_name = emote.split(':')[2][:-1]
                anim = emote.split(':')[0]
                if anim == '<a':
                    url = f'https://cdn.discordapp.com/emojis/{emoji_name}.gif'
                else:
                    url = f'https://cdn.discordapp.com/emojis/{emoji_name}.png'
                try:
                    response = requests.get(url)
                    img = response.content
                    emote = await ctx.guild.create_custom_emoji(name=name,
                                                                image=img)
                    return await ctx.send(
                        embed=discord.Embed(title="emoji-add",
                                            description="added \"**`%s`**\"!" %
                                            (emote),
                                            color=0x2f3136))
                except Exception:
                    return await ctx.send(
                        embed=discord.Embed(title="emoji-add",
                                            description=f"failed to add emoji",
                                            color=0x2f3136))
            else:
                return await ctx.send(
                    embed=discord.Embed(title="emoji-add",
                                        description=f"invalid emoji",
                                        color=0x2f3136))
        except Exception:
            return await ctx.send(
                embed=discord.Embed(title="emoji-add",
                                    description=f"failed to add emoji",
                                    color=0x2f3136))

    @commands.group(name="emoji-delete",
                      description="Deletes a emoji",
                      usage="emoji-delete [emoji]",
                      aliases=["edel"])
    @commands.has_permissions(manage_emojis=True)
    async def deleteemoji(self, ctx, emote: discord.Emoji):
        return await ctx.send(
            embed=discord.Embed(title="emoji-delete",
                                description="deleted \"**`%s`**\"!" % (emote),
                                color=0x2f3136))

def setup(bot):
    bot.add_cog(general(bot))
