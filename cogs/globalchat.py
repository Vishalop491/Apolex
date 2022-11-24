import discord
from discord.ext import commands
import json

class invites67(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Global chat commands"""
  
    def help_custom(self):
		      emoji = '<:greystar:1015912650498134066>  '
		      label = "Global chat"
		      description = ""
		      return emoji, label, description
#')


    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def __Globalchat__(self, ctx: commands.Context):
        """• `globalchatstart`, `globalchatstop`"""
       # await ctx.send('leveling is under construction.')
    

    
    #@commands.command()
    ##async def level(self, ctx: commands.Context, user: discord.Member):
     #   with open('./data/databases/leveling.json', 'r') as f:
           # leveling = json.load(f)
       # await ctx.send(f'{user.mention} is currently level {leveling[str(user.id)]["level"]}.')

def setup(bot):
    bot.add_cog(invites67(bot))