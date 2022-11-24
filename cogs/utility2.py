import discord
from discord.ext import commands
import json

class utility67(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Utility commands"""  

    def help_custom(self):
		      emoji = '<:iaoakwk:989088650316902400>'
		      label = "Utility"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def __Utility__(self, ctx: commands.Context):
        """• `todo`, `todo list`, `todo add`, `todo remove`, `todo clear`, `banner-user`, `banner server`, `translate <lang> <msg>`, `status`, `newembed`, `github`, `suggest`, `report`, `auditlog <entries>`, `steal`, `emoji-delete`, `list-bots`, `role list`, `nuke`, `firstmessage`, `autosnipe channel`, `autosnipe config`, `autosnipe delete`, `note`, `notes`, `trashnotes`, `vcdeafen`, `vcundeafen`, `vcmute`, `vcunmute`, `vckick`, `vchide`, `tempban <user> <time> eg. tempban <you> <1 d>`, `hackban`, `fuckoff`, `jana`, `getlost`, `moveall`, `give <user> <role>`, `role temp <role> <time> <user>`, `role remove <user> <role>`, `role delete <role>`, `role create <name>`, `role rename <role> <new name>`, `role color <role> <color>`, `roleinfo <role>`"""
       # await ctx.send('leveling is under construction.')
    

    
    #@commands.command()
    ##async def level(self, ctx: commands.Context, user: discord.Member):
     #   with open('./data/databases/leveling.json', 'r') as f:
           # leveling = json.load(f)
       # await ctx.send(f'{user.mention} is currently level {leveling[str(user.id)]["level"]}.')

def setup(bot):
    bot.add_cog(utility67(bot))