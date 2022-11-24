import discord
from discord.ext import commands
import json

class reactionrole67(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """SelfRoles commands"""  

    def help_custom(self):
		      emoji = '<:StoregeGrey:1015913762152267838> '
		      label = "Self Roles"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def __ReactionRole__(self, ctx: commands.Context):
        """• `reaction <emote> <role> <channel> <title>`, `reactions`"""
       # await ctx.send('leveling is under construction.')
    

    
    #@commands.command()
    ##async def level(self, ctx: commands.Context, user: discord.Member):
     #   with open('./data/databases/leveling.json', 'r') as f:
           # leveling = json.load(f)
       # await ctx.send(f'{user.mention} is currently level {leveling[str(user.id)]["level"]}.')

def setup(bot):
    bot.add_cog(reactionrole67(bot))