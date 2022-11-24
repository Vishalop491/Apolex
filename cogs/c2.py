import discord
from discord.ext import commands
import json

class fun870(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Vc Roles"""
  
    def help_custom(self):
		      emoji = '<:grey_microphone:1019254423689633842>'
		      label = "Vc Roles"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def __VcRoles__(self, ctx: commands.Context):
        """• `vcroles new`, `vcrole config`, `vcrole delete` """
       # await ctx.send('leveling is under construction.')
    

    
    #@commands.command()
    ##async def level(self, ctx: commands.Context, user: discord.Member):
     #   with open('./data/databases/leveling.json', 'r') as f:
           # leveling = json.load(f)
       # await ctx.send(f'{user.mention} is currently level {leveling[str(user.id)]["level"]}.')

def setup(bot):
    bot.add_cog(fun870(bot))