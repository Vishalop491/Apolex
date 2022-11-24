import discord
from discord.ext import commands
import json

class ticket67(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

   # """Ticket commands"""  

    def help_custom(self):
		      emoji = '<:top2:1015918779009613854>'
		      label = "Ticket"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def __Tickets__(self, ctx: commands.Context):
        """• `sendpanel`, `adduser`"""
       # await ctx.send('leveling is under construction.')
    

    
    #@commands.command()
    ##async def level(self, ctx: commands.Context, user: discord.Member):
     #   with open('./data/databases/leveling.json', 'r') as f:
           # leveling = json.load(f)
       # await ctx.send(f'{user.mention} is currently level {leveling[str(user.id)]["level"]}.')

def setup(bot):
    bot.add_cog(ticket67(bot))