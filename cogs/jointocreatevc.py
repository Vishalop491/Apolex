import discord
from discord.ext import commands
import json

class j2c(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """J2C commands"""

    def help_custom(self):
		      emoji = '<:greymic:1015913434916855909>'
		      label = "Join To Create"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def __JoinToCreate__(self, ctx: commands.Context):
        """• `voice setupj2c`, `voice claim`, `voice lock`, `voice unlock`, `voice permit <@user>`, `voice reject <@user>`, `voice name <new channel name>`, `voice limit (Eg 1,2,3)`"""
       # await ctx.send('leveling is under construction.')
    

    
    #@commands.command()
    ##async def level(self, ctx: commands.Context, user: discord.Member):
     #   with open('./data/databases/leveling.json', 'r') as f:
           # leveling = json.load(f)
       # await ctx.send(f'{user.mention} is currently level {leveling[str(user.id)]["level"]}.')

def setup(bot):
    bot.add_cog(j2c(bot))