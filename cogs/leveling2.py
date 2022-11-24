import discord
from discord.ext import commands
import json

class Leveling2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Antinuke commands"""
  
    def help_custom(self):
		      emoji = '<:IconPublicSecurity:1015920331048886352>'
		      label  = "Antinuke"
		      description = ""
		      return emoji, label, description  

#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def __Antinuke__(self, ctx: commands.Context):
        """• `anti vanity steal`, `anti ban`, `anti bot`, `anti channel create`, `anti channel delete`, `anti channel update`, `anti guild update`, `anti kick`, `anti member update`, `anti role create`, `anti role delete`, `anti role update`, `anti webhook`, `features`, `channelclean`, `roleclean`, `whitelist`, `unwhitelist`, `whitelised`, `setvanity`"""
       # await ctx.send('leveling is under construction.')
    

    
    #@commands.command()
    ##async def level(self, ctx: commands.Context, user: discord.Member):
     #   with open('./data/databases/leveling.json', 'r') as f:
           # leveling = json.load(f)
       # await ctx.send(f'{user.mention} is currently level {leveling[str(user.id)]["level"]}.')

def setup(bot):
    bot.add_cog(Leveling2(bot))