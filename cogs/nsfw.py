import discord
import logging
import aiohttp
from discord.ext import commands
import motor.motor_asyncio as mongodb
from discord.colour import Color

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)

class nsfw(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.color = 0x2f3136
        self.connection = mongodb.AsyncIOMotorClient("mongodb+srv://hacker:chetan2004@secure.9rv0s.mongodb.net/secure?retryWrites=true&w=majority")
        self.db = self.connection["secure"]["servers"]
        

    async def get_image(self, type):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://nekobot.xyz/api/image?type=%s" % (type)) as response:
                json = await response.json()
                if json["success"]:
                    return json["message"]
                else:
                    return "Failed"


    
    @commands.group(name="hass", description="NSFW", usage="nsfw hass")
    async def hass(self, ctx):
        url = await self.get_image(type="hass")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="hmidriff", description="NSFW", usage="nsfw hmidriff")
    async def hmidriff(self, ctx):
        url = await self.get_image(type="hmidriff")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="pgif", description="NSFW", usage="nsfw pgif")
    async def pgif(self, ctx):
        url = await self.get_image(type="pgif")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="4k", description="NSFW", usage="nsfw 4k")
    async def fourk(self, ctx):
        url = await self.get_image(type="4k")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="holo", description="NSFW", usage="nsfw holo")
    async def holo(self, ctx):
        url = await self.get_image(type="holo")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="hneko", description="NSFW", usage="nsfw hneko")
    async def hneko(self, ctx):
        url = await self.get_image(type="hneko")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="neko", description="NSFW", usage="nsfw neko")
    async def neko(self, ctx):
        url = await self.get_image(type="neko")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="hkitsune", description="NSFW", usage="nsfw hkitsune")
    async def hkitsune(self, ctx):
        url = await self.get_image(type="hkitsune")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="kemonomimi", description="NSFW", usage="nsfw kemonomimi")
    async def kemonomimi(self, ctx):
        url = await self.get_image(type="kemonomimi")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="anal", description="NSFW", usage="nsfw anal")
    async def anal(self, ctx):
        url = await self.get_image(type="anal")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="hanal", description="NSFW", usage="nsfw hanal")
    async def hanal(self, ctx):
        url = await self.get_image(type="hanal")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="gonewild", description="NSFW", usage="nsfw gonewild")
    async def gonewild(self, ctx):
        url = await self.get_image(type="gonewild")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="kanna", description="NSFW", usage="nsfw kanna")
    async def kanna(self, ctx):
        url = await self.get_image(type="kanna")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="ass", description="NSFW", usage="nsfw ass")
    async def ass(self, ctx):
        url = await self.get_image(type="ass")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="pussy", description="NSFW", usage="nsfw pussy")
    async def pussy(self, ctx):
        url = await self.get_image(type="pussy")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="thigh", description="NSFW", usage="nsfw thigh")
    async def thigh(self, ctx):
        url = await self.get_image(type="thigh")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="hthigh", description="NSFW", usage="nsfw hthigh")
    async def hthigh(self, ctx):
        url = await self.get_image(type="hthigh")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="gah", description="NSFW", usage="nsfw gah")
    async def gah(self, ctx):
        url = await self.get_image(type="gah")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="food", description="NSFW", usage="nsfw food")
    async def food(self, ctx):
        url = await self.get_image(type="food")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="paizuri", description="NSFW", usage="nsfw paizuri")
    async def paizuri(self, ctx):
        url = await self.get_image(type="paizuri")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="tentacle", description="NSFW", usage="nsfw tentacle")
    async def tentacle(self, ctx):
        url = await self.get_image(type="tentacle")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="boobs", description="NSFW", usage="nsfw boobs")
    async def boobs(self, ctx):
        url = await self.get_image(type="boobs")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="hboobs", description="NSFW", usage="nsfw hboobs")
    async def hboobs(self, ctx):
        url = await self.get_image(type="hboobs")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="yaoi", description="NSFW", usage="nsfw yaoi")
    async def yaoi(self, ctx):
        url = await self.get_image(type="yaoi")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))


    @commands.group(name="random", description="NSFW", usage="nsfw random")
    async def random(self, ctx):
        url = await self.get_image(type="random")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color)) 



    @commands.group(name="lesbian", description="NSFW", usage="nsfw lesbian")
    async def lesbian(self, ctx):
        url = await self.get_image(type="lesbian")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color)) 


    @commands.group(name="nudes", description="NSFW", usage="nsfw nudes")
    async def nudes(self, ctx):
        url = await self.get_image(type="nudes")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))  


    @commands.group(name="blowjob", description="NSFW", usage="nsfw blowjob")
    async def blowjob(self, ctx):
        url = await self.get_image(type="blowjob")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))
          

    @commands.group(name="tits", description="NSFW", usage="nsfw tits")
    async def tits(self, ctx):
        url = await self.get_image(type="tits")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))

    @commands.group(name="feet", description="NSFW", usage="nsfw feet")
    async def feet(self, ctx):
        url = await self.get_image(type="feet")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color)) 

          
    @commands.group(name="dick", description="NSFW", usage="nsfw dick")
    async def dick(self, ctx):
        url = await self.get_image(type="dick")
        if ctx.channel.is_nsfw(): await ctx.send(embed=discord.Embed(title="nsfw", color=self.color).set_image(url=url))
        if ctx.channel.is_nsfw() != True: return await ctx.send(embed=discord.Embed(title="NSFW", description="**`%s`** does not have nsfw mode enabled" % (ctx.channel.name), color=self.color))    

          
def setup(bot):
    bot.add_cog(nsfw(bot))
