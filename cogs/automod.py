import discord
from discord.ext import commands
import json

class ticket670(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Automod commands"""  

    def help_custom(self):
		      emoji = '<:op2:1015918352855732285>  '
		      label = "Automod"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def __Automod__(self, ctx: commands.Context):
        """• `antilink enable,` `antilink disable`, `antimassping enable`, `antimassping disable`, `ping-limit-set`, `ping-limit-show`, `antispam enable`, `antispam disable`"""
       # await ctx.send('leveling is under construction.')
    

    
    #@commands.command()
    ##async def level(self, ctx: commands.Context, user: discord.Member):
     #   with open('./data/databases/leveling.json', 'r') as f:
           # leveling = json.load(f)
       # await ctx.send(f'{user.mention} is currently level {leveling[str(user.id)]["level"]}.')

def setup(bot):
    bot.add_cog(ticket670(bot))