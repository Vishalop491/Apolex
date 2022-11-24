import discord
import json
from discord.ext import commands
from discord.ui import Button, View
from .utils.config import *

class errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

      


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        missing = ", ".join(error.args)
        await ctx.send(f"<:hajaks:989006655511478294> | {missing}", delete_after=10)
      elif isinstance(error, commands.MissingPermissions):
        missing_perms = ", ".join(error.missing_perms)
        await ctx.send(f"<:hajaks:989006655511478294> | You don't have the {missing_perms} permisisons to run the **{ctx.command.name}** command!", delete_after=10)
      elif isinstance(error, commands.MemberNotFound):
          await ctx.send(f"<:hajaks:989006655511478294> | Please provide a member!", delete_after=10)
      elif isinstance(error, commands.NSFWChannelRequired):
        em6 = discord.Embed(description=f"<:hajaks:989006655511478294> | Please first enable NSFW Channel in this channel!", color = discord.Colour.dark_red(), timestamp=ctx.message.created_at)
        em6.set_image(url=f"https://i.imgur.com/oe4iK5i.gif")

        await ctx.send(embed=em6, delete_after=10)
      elif isinstance(error, commands.BotMissingPermissions):
        missing = ", ".join(error.missing_perms)
        await ctx.send(f'<:hajaks:989006655511478294> | I need the **{missing}** to run the **{ctx.command.name}** command!', delete_after=10)
      elif isinstance(error, commands.CommandNotFound):
        print(" ")
      else:
        raise error

    @commands.Cog.listener()
    async def on_message(self, message):
      with open("prefixes.json", "r") as f:
       idk = json.load(f)
       if str(message.guild.id) in idk:
        idkprefix = idk[str(message.guild.id)]
        if str(self.bot.user.id) in message.content:
          b = Button(label='Vote Me', style=discord.ButtonStyle.link, url='https://top.gg/bot/992797622094016622/vote')
          b2 = Button(label='Support', style=discord.ButtonStyle.link, url='https://discord.gg/apolex')
          b3 = Button(label='invite', style=discord.ButtonStyle.link, url='https://discord.com/oauth2/authorize?client_id=992797622094016622&permissions=8&scope=bot')          
          view = View()
          view.add_item(b)
          view.add_item(b2)
          view.add_item(b3)
          embed = discord.Embed(title='Hey, I am apolex', description=f'To view my commands type `{idkprefix}help` You can change my prefix using `{idkprefix}setprefix <new prefix>`\n\nIf you continue to have problems, consider asking for help in our [headquarters](https://discord.gg/94yybZQU7B)・[vote](https://top.gg/bot/992797622094016622/vote)', color=0x2f3136)
          await message.channel.send(embed=embed, view=view)

def setup(bot):
    bot.add_cog(errors(bot))