import discord
from discord.ext import commands
import json

class fun67(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Fun commands"""
  
    def help_custom(self):
		      emoji = '<:top3:1015918807170175026>'
		      label = "Fun"
		      description = ""
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def __Fun__(self, ctx: commands.Context):
        """• `urban`, `fight`, `akinator`, `asktrump`, `channelinfo`, `getemotes`, `meme`, `aw`, `info`, `avatar`, `servericon`, `invite`, `membercount`, `slap`,  `pat`, `inspire`, `poll`, `hack`, `wizz`, `gay`, `typerace`, `truth`, `dare`, `blackjack`, `pokemon`, `pikachu`, `8ball`, `badges`, `findimposter`, `rps`, `hangman`, `tictactoe`, `reverse`, `roll`, `source`"""
       # await ctx.send('leveling is under construction.')
     #   embed.set_thumbnail(url = "https://images-ext-1.discordapp.net/external/cAtd1tILoERtU1SBq7qQIbfyXJMdtOoftjcjw7HoS8c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png")
    

    
    #@commands.command()
    ##async def level(self, ctx: commands.Context, user: discord.Member):
     #   with open('./data/databases/leveling.json', 'r') as f:
           # leveling = json.load(f)
       # await ctx.send(f'{user.mention} is currently level {leveling[str(user.id)]["level"]}.')

def setup(bot):
    bot.add_cog(fun67(bot))