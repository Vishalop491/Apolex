import discord
from discord.ext import commands
import json

class NSFW2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Nsfw commands"""
  
    def help_custom(self):
		      emoji = '<:channel_nsfw:1015915678093541497> '
		      label = "Nsfw"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def __Nsfw__(self, ctx: commands.Context):
        """• `nsfw4k`, `nsfwpussy`, `nsfwboobs`, `nsfwlewd`, `nsfwlesbian`, `nsfwblowjob`, `nsfwcum`, `nsfwgasm`, `nsfwhentai`"""
       # await ctx.send('leveling is under construction.')
    

    
    #@commands.command()
    ##async def level(self, ctx: commands.Context, user: discord.Member):
     #   with open('./data/databases/leveling.json', 'r') as f:
           # leveling = json.load(f)
       # await ctx.send(f'{user.mention} is currently level {leveling[str(user.id)]["level"]}.')

def setup(bot):
    bot.add_cog(NSFW2(bot))