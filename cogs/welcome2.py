import discord
from discord.ext import commands
import json

class logging6799(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Welcome commands"""  

    def help_custom(self):
		      emoji = '<:member:1015921230785814568>'
		      label = "Welcome"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def __Welcomes__(self, ctx: commands.Context):
        """• `joinchannel`, `removechannel`, `resetall`, `top`, `invites`, `greet`, `greetdel`, `welcome enable`, `welcome disable`, `welcome channel`, `welcome test`, `welcome message`, `leave channel`, `leave config`, `leave delete`, `autorole add`, `autorole humans`, `autorole bots`, `autorole delete`, `autorole botsdelete`, `autorole humansdelete`\n\nWelcome variables\n`++user.name++`, `++user.mention++`, `++user.id++`, `++user.tag++`, `++server.name++`, `++server.membercount++`"""
       # await ctx.send('leveling is under construction.')
    

    
    #@commands.command()
    ##async def level(self, ctx: commands.Context, user: discord.Member):
     #   with open('./data/databases/leveling.json', 'r') as f:
           # leveling = json.load(f)
       # await ctx.send(f'{user.mention} is currently level {leveling[str(user.id)]["level"]}.')

def setup(bot):
    bot.add_cog(logging6799(bot))