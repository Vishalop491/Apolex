import string
import discord
import json
from discord.ui import Button, View
import asyncio
from .utils.config import DEFAULT_COLOR
from discord.ext import commands
from datetime import datetime, timedelta
from itertools import cycle
from views import help as vhelp #need big refactor

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

class HelpCommand(commands.HelpCommand):
    """Help command"""


  
    async def on_help_command_error(self, ctx, error) -> None:
        handledErrors = [
            commands.CommandOnCooldown, 
            commands.CommandNotFound
        ]

        if not type(error) in handledErrors:
            print("! Help command Error :", error, type(error), type(error).__name__)
            return await super().on_help_command_error(ctx, error)

    def command_not_found(self, string) -> None:
        raise commands.CommandNotFound(f"Command {string} is not found")

    async def send_bot_help(self, mapping) -> None:
        allowed = 5
        close_in = round(datetime.timestamp(datetime.now() + timedelta(minutes=allowed)))
    
        embed = discord.Embed(color = 0x2f3136,title = f"Help Menu", description=f"""
• Total commands: 286 | Usable by you (here): 200
• You can change my prefix using !setprefix <prefix>.


Made by: Apolex Development
Prefix: !

__**Main**__
<:grey_microphone:1019254423689633842> Vc Roles
<:CH_IconGreyGift:1015920090094501938> Giveaway
<:IconGreyPin:1019249839738982490> Icon
<:greymic:1015913434916855909> Join To Create
<:IconPublicSecurity:1015920331048886352> Antinuke
<:ak:1015886373301006397> Logging
<:member:1015921230785814568> Welcome
<:top2:1015918779009613854> Ticket

__**Extras**__
<:StoregeGrey:1015913762152267838> Self Roles
<:channel_nsfw:1015915678093541497> Nsfw
<:greystar:1015912650498134066> Global Chat
<:op2:1015918352855732285> Automod
<:top3:1015918807170175026> Fun
<:iaoakwk:989088650316902400> Utility
<:op3:1015918436351754240> Moderation
""")
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/990170312110931988/1003985383211667496/SPOILER_anbot.png") 
        embed.set_footer(text=f"Made With 💖 By Team Apolex", icon_url="https://images-ext-1.discordapp.net/external/FzODk5rco611Nu1reLadr8OVpXubmmw-_98eFFr3J8M/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/973137921999765515/62c64e7b9afba7292ade5f06a5f0ad11.png")
        embed.set_author(name=f"Apolex", icon_url="https://cdn.discordapp.com/attachments/990170312110931988/1003985383211667496/SPOILER_anbot.png")
      #  embed.set_author(name=f"{self.bot.user.name}", icon_url=f"{self.bot.user.avatar}")#        embed.set_image(url="https://cdn.discordapp.com/attachments/98187760embed.set_author(name=f"{self.bot.user.name} Bot Stats", icon_url=self.bot.user.display_avatar.url)7597481989/983972390973349958/standard_4.gif")
        #embed.set_footer(text=f"")
       # embed.set_author(name=f"{bot.user.name}", icon_url=f"{bot.avatar}")

        view = vhelp.View(mapping = mapping, ctx = self.context, homeembed = embed, ui = 2)
        message = await self.context.send(embed = embed, view = view)
        try:
            await asyncio.sleep(60*allowed)
            view.stop()
            await message.delete()
        except: pass
 
    async def send_command_help(self, command):
        cog = command.cog
        if "help_custom" in dir(cog):
            label, _ = cog.help_custom()
            embed = discord.Embed(title = f"Help · {label} : {command.name}", description=f"**Command** : {command.name}\n{command.help}", url="https://discord.gg/apolex", color = 0x2f3136)
            params = ""
            for param in command.clean_params: 
                params += f" <{param}>"
            embed.add_field(name="Usage", value=f"{command.name}{params}", inline=False)
            embed.add_field(name="Aliases", value=f"{command.aliases}`")
            embed.set_footer(text="Remind : Hooks such as <> must not be used when executing commands.", icon_url=self.context.message.author.display_avatar.url)
            await self.context.send(embed=embed, color=0x2f3136)

    async def send_cog_help(self, cog):
        if "help_custom" in dir(cog):
            label, _ = cog.help_custom()
            embed = discord.Embed(title = f"Help", url="https://discord.gg/tsop", color = 0x2f3136)
            for command in cog.get_commands():
                params = ""
                for param in command.clean_params: 
                    params += f" <{param}>"
                embed.add_field(name=f"{command.name}{params}", value=f"{command.help}\n\u200b", inline=False)
            embed.set_footer(text="Remind : Hooks such as <> must not be used when executing commands.", icon_url=self.context.message.author.display_avatar.url, color = 0x2f3136)
            await self.context.send(embed=embed, color = 0x2f3136)

    async def send_group_help(self, group):
        await self.context.send("Group commands unavailable.")
     

class Help(commands.Cog, name="help"):
    """Help commands."""
    def __init__(self, bot):
        self._original_help_command = bot.help_command

        attributes = {
            'name': "help",
            'aliases': ['h'],
            'cooldown': commands.CooldownMapping.from_cooldown(1, 5, commands.BucketType.user) # discordpy2.0
        } 

        bot.help_command = HelpCommand(command_attrs=attributes)
        bot.help_command.cog = self
        
    def cog_unload(self):
        self.bot.help_command = self._original_help_command

    def help_custom(self):
        emoji = '<:greyrules:1015912713374941244>'
        label = "Help"
        description = ""
        return emoji, label, description

def setup(bot):
	bot.add_cog(Help(bot))