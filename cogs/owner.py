import contextlib
from traceback import format_exception
import discord
from discord.ext import commands
from .utils.config import *
import io
import textwrap
import json
import datetime
import sys
import jishaku
from discord.ui import Button, View
import psutil
import time
import platform



class owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.load_extension('jishaku')
        jishaku.Flags.NO_DM_TRACEBACK = True
        jishaku.Flags.NO_UNDERSCORE = True

  
  
    @commands.group(name='eval', invoke_without_command=True)
    @commands.is_owner()
    async def _infinity(self, ctx: commands.Context):
        guilds = len(self.bot.guilds)
        users = len(set(self.bot.get_all_members()))
        channels = len(set(self.bot.get_all_channels()))
        owner = self.bot.get_user(self.bot.owner_ids[0])
        em = discord.Embed(title='<:icons_text1:986851468097253417> Eval', description=f'<:icons_text1:986851468097253417> discord.py `{discord.__version__}`\n<:icons_text1:986851468097253417> python version {sys.version}\n<:icons_text1:986851468097253417>\n<:icons_text1:986851468097253417> **{guilds}** guilds\n<:icons_text1:986851468097253417> **{users}** users\n<:icons_text1:986851468097253417> **{channels}** channels', color=0x2f3136)
        em.set_footer(text=f'{owner}', icon_url=owner.avatar)
        await ctx.send(embed=em)
        
    @_infinity.command(aliases=['python'])
    @commands.is_owner()
    async def py(self, ctx: commands.Context, *, code):
        code = clean_code(content=code)
        local_variables = {
            "discord": discord,
            "commands": commands,
            "bot": self.bot,
            "ctx": ctx,
            "message": ctx.message,
            "channel": ctx.channel,
            "author": ctx.author,
            "guild": ctx.guild,
            "message": ctx.message,
            "self": self,
        }

        stdout = io.StringIO()
        try:
            with contextlib.redirect_stdout(stdout):
                exec(
                    f"async def func():\n{textwrap.indent(code, '   ')}", local_variables
                )

                obj = await local_variables["func"]()
                result = f"{stdout.getvalue()}\n-- {obj}"
        except Exception as e:
            result = "".join(format_exception(e, e, e.__traceback__))

        await ctx.send(f'```py\n{result}\n```')

    @_infinity.command(aliases=['reload'])
    @commands.is_owner()
    async def _reload(self, ctx: commands.Context, *, cog: str):
        try:
            self.bot.reload_extension(cog)
            await ctx.send(f"Reloaded {cog}")
        except Exception as e:
            await ctx.send(f"Failed to reload {cog}\n Error: {e}")
    
    @_infinity.command(aliases=['load'])
    @commands.is_owner()
    async def _load(self, ctx: commands.Context, *, cog: str):
        try:
            self.bot.load_extension(cog)
            await ctx.send(f"Loaded {cog}")
        except Exception as e:
            await ctx.send(f"Failed to load {cog}\n Error: {e}")
    
    @_infinity.command(aliases=['unload'])
    @commands.is_owner()
    async def _unload(self, ctx: commands.Context, *, cog: str):
        try:
            self.bot.unload_extension(cog)
            await ctx.send(f"Unloaded {cog}")
        except Exception as e:
            await ctx.send(f"Failed to unload {cog}\n Error: {e}")

    @_infinity.command(aliases=['dbg'])
    async def debug(self, ctx: commands.Context, *, command: str):
        command = self.bot.get_command(command)
        
        if command is None:
            await ctx.send("Command not found")
            return
        
        try:
            await ctx.invoke(command)
        except Exception as e:
            await ctx.send(f"```py\n{e.__traceback__}\n```")


    @commands.command(name="stats", aliases=["statistics", "botinfo"], usage='stats', brief='!stats')
    async def stats(self, ctx):
        """Shows some usefull information about PyBot"""
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.bot.guilds)
        # revision = self.get_last_commits()
 
        total_memory = psutil.virtual_memory().total >> 20
        used_memory = psutil.virtual_memory().used >> 20
        cpu_used = str(psutil.cpu_percent())
 
 
        total_members = sum(g.member_count for g in self.bot.guilds if g.member_count != None)
        cached_members = len(self.bot.users)
 
        a = Button(label='Invite Me', style=discord.ButtonStyle.link, url='https://discord.com/api/oauth2/authorize?client_id=992797622094016622&permissions=8&scope=bot')
        
        b = Button(label='Vote Me', style=discord.ButtonStyle.link, url='https://top.gg/bot/992797622094016622/vote')
        view = View()
        view.add_item(a)
        view.add_item(b)
 
        embed = discord.Embed(colour=0x2f3136)
 
         #embed.add_field(name='General Info', value=f"""```asciidoc
#Total servers - {serverCount}
#Total shards - {len(self.bot.shards)} 

#Total members - {total_members}
#Total cached members - {cached_members}

##Total Used Memory - {used_memory}
#Total Memory - {total_memory}
#Total CPU - {cpu_used}% used
#Total Bot Ping - {round(self.bot.latency * 600, 2)}

##Python - {pythonVersion}
#Discord.py - {discord.__version__}
#```""")start_time = calendar.timegm(time.strptime(start_time.strftime("%Y-%m-%d %H:%M:%S+00:00"), '%Y-%m-%d %H:%M:%S+00:00'))
 
        embed.add_field(name='Apx', value=f"""
**Server(s)**
```asciidoc
Total servers - {serverCount}
Total shard servers - {serverCount}
Total shards - {len(self.bot.shards)}```
**Member(s)**
```asciidoc
Total members - {total_members}
Total cached members - {cached_members}```
**Memor(y)**
```asciidoc
Total Used Memory - {used_memory}
Total Memory - {total_memory}
Total CPU - {cpu_used}% used
Total Bot Ping - {round(self.bot.latency * 600, 2)}```
**Veriso(n)**
```asciidoc
Python Verison - {pythonVersion}
Discord.py Verison - {discord.__version__}```

**Developer(s)**
[ArchDuke](https://discord.com/users/963973437427175434), [Vivox](https://discord.com/users/973137921999765515)

**Owner(s)**
[TecnoPlayZ](https://discord.com/users/985054981910581288), [Ros Op](https://discord.com/users/878667191157915669), [Diabolus](https://discord.com/users/177932282559070208), [Ghost](https://discord.com/users/775600697911148555), [Godking](https://discord.com/users/797116201595568138)""")
        
       # embed.add_field(name="System Info", value=f"""```asciidoc
#Total Used Memory - {used_memory}
#Total Memory - {total_memory}
#Total CPU - {cpu_used}% used
#Total Bot Ping - {round(self.bot.latency * 600, 2)}```""")
      ##  embed.add_field(name='Version Info', value=f"""```asciidoc
#```""")
        ##embed.add_field(
         #   name="Bot Stats",
          #  value=f"Ping: {round(self.bot.latency * 1000, 2)}ms")
        # embed.add_field(name="System", value=f"**RAM**: {used_memory}/{total_memory} MB\n**CPU:** {cpu_used}% used.", inline=False),
        # embed.add_field(name='Version', value=f'Python - {pythonVersion}\nDiscordPY - {dpyVersion}', inline=False)
        anshuman = await self.bot.fetch_user(973137921999765515)
        if anshuman in ctx.guild.members:
            a = f'{anshuman.mention}'
        else:
            a = f'{anshuman}'
        #embed.add_field(name=' Developers', value=f"[ArchDuke](https://discord.com/users/963973437427175434)\n[Vivox](https://discord.com/users/973137921999765515)")
       # embed.add_field(name='Bot Owners', value=f"\n[TecnoPlayZ](https://discord.com/users/985054981910581288)\n[Ros Op](https://discord.com/users/878667191157915669)\n[Diabolus](https://discord.com/users/177932282559070208)\n[Sangrash](https://discord.com/users/823550474593501214)\n[Ghost](https://discord.com/users/775600697911148555)\n[Godking](https://discord.com/users/797116201595568138)")
        embed.set_author(name=f"{self.bot.user.name} Bot Stats", icon_url=self.bot.user.display_avatar.url)
        # embed.add_field(name='Latest Changes', value=revision, inline=False)

        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/990170312110931988/1003985383211667496/SPOILER_anbot.png")
        embed.set_footer(text='Made With 💖 By Team Apolex')
 
        await ctx.send(embed=embed, view=view)


def setup(bot):
    bot.add_cog(owner(bot))