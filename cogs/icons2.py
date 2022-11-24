import discord
from discord.ext import commands
import json

class icon67(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Icon commands"""  

    def help_custom(self):
		      emoji = '<:IconGreyPin:1019249839738982490>'
		      label = "Icon"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def __Icon__(self, ctx: commands.Context):
        """• `banners`, `pfps`, `boyspng`, `boysgif`, `girlspng`, `girlsgif`, `couplespng`, `couplesgif`, `animepng`, `animegif`"""
       # await ctx.send('leveling is under construction.')
    

    
    #@commands.command()
    ##async def level(self, ctx: commands.Context, user: discord.Member):
     #   with open('./data/databases/leveling.json', 'r') as f:
           # leveling = json.load(f)
       # await ctx.send(f'{user.mention} is currently level {leveling[str(user.id)]["level"]}.')

def setup(bot):
    bot.add_cog(icon67(bot))