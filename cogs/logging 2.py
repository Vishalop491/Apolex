import discord
from discord.ext import commands
import json

class logging67(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Logging commands"""  

    def help_custom(self):
		      emoji = '<:ak:1015886373301006397>'
		      label = "Logging"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def __Logging__(self, ctx: commands.Context):
        """• `logging channel`, `logging config`, `logging delete`"""
       # await ctx.send('leveling is under construction.')
    

    
    #@commands.command()
    ##async def level(self, ctx: commands.Context, user: discord.Member):
     #   with open('./data/databases/leveling.json', 'r') as f:
           # leveling = json.load(f)
       # await ctx.send(f'{user.mention} is currently level {leveling[str(user.id)]["level"]}.')

def setup(bot):
    bot.add_cog(logging67(bot))