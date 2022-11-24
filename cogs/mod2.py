import discord
from discord.ext import commands
import json

class Moderation2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Moderation commands"""
  
    def help_custom(self):
		      emoji = '<:op3:1015918436351754240> '
		      label  = "Moderation"
		      description = ""
		      return emoji, label, description  

#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def __Moderation__(self, ctx: commands.Context):
        """• `selfrole`, `verification`, `setprefix`, `addchannel`, `deletechannel`, `hide`, `unhide`, `lockserver`, `ban`, `unban`, `warn`, `timeout`, `mute`, `unmute`, `nick`, `lockall`, `unlockall`, `lock`, `unlock`, `hideall`, `unhideall`, `purge`, `purge contains`, `purge startswith`, `purge endswith`, `purge user`, `purge invites`, `clean embeds`, `clean files`, `clean bots`, `clean emojis`, `clean images`, `clean reactions`, `clean all`, `clean mentions`, `clone`, `slowmode`, `snipe`, `enlarge`, `roleall`, `roleallhumans`, `roleallbots`, `removeallhumans`, `removeallbots`, `jail`, `unjail`, `boosts`, `cleanup (Clears Bot Messages)`, `unbanall`  """
       # await ctx.send('leveling is under construction.')
    

    
    #@commands.command()
    ##async def level(self, ctx: commands.Context, user: discord.Member):
     #   with open('./data/databases/leveling.json', 'r') as f:
           # leveling = json.load(f)
       # await ctx.send(f'{user.mention} is currently level {leveling[str(user.id)]["level"]}.')

def setup(bot):
    bot.add_cog(Moderation2(bot))