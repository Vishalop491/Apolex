import discord
import httpx
import aiohttp
#from aiohttp import ClientSession
from io import BytesIO
import os
import asyncio
from itertools import cycle
#from ext.paginator import PaginatorSession
from discord.ext import commands
import humanfriendly
import datetime
from discord.ext import commands
#import aiohttp
import discord
#from discord import ApplicationContext
from cogs.utils.lister import lister
from io import BytesIO

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tasks = []
      
    @commands.command(
        name='nuke',
        description='Remakes current channel.',
        aliases=['nukechannel'],
        usage="nuke"
    )
    @commands.cooldown(1, 30, commands.BucketType.guild)
    @commands.has_permissions(manage_channels=True)
    async def nuke(self, ctx, arg=None):
            extras = "!"
            await ctx.message.delete()
            if arg != None:
                await ctx.send(
                    ('Invalid command usage, please use `' + ' and '.join(extras) + 'nuke` to re-create the current channel.'), delete_after=10)
            else:
                counter = 0
                await ctx.send((f"<:sowlbz:989006711920668703> | Nuking Channel {ctx.channel.name}..."))
                channel_info = [ctx.channel.category,
                ctx.channel.position]
                channel_id = ctx.channel.id
                await ctx.channel.clone()
                await ctx.channel.delete()
                new_channel = channel_info[0].text_channels[-1]
                await new_channel.edit(position=channel_info[1])
                embed = discord.Embed(colour=0x2f3136, timestamp=ctx.message.created_at)
                embed.set_author(name=f"Channel Nuked.", icon_url=ctx.author.avatar.url)
                embed.set_footer(text=f"{ctx.author}")
                embed.set_image(url="https://cdn.discordapp.com/attachments/943391406347653160/946065442303275008/ELs8.gif")
                await new_channel.send(embed=embed)

  

        
    @commands.command(
        name='banlist',
        description='Returns the server\'s banlist',
        usage="banlist",
        aliases=["banned", "bannedusers"]
        )
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def banlist(self, ctx):
      list = ctx.guild.bans()
      banned = ""
      count = 0

      if len(list) > 0:
        for ban in list:
            user = ban.user

            count += 1
            banned += f"\n{count} Banned user(s)\nName(s): {user.name}#{user.discriminator}\nuser id(s){user.id}\n\n"
        embed1 = discord.Embed(title=f'Apole+X', url = 'https://discord.com/api/oauth2/authorize?client_id=992797622094016622&permissions=8&scope=bot',description =banned, color=0x2f3136)
        embed1.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}')
        await ctx.send(embed = embed1) 
      else:
        embed2 = discord.Embed(title=f'Apole+X', url = 'https://discord.com/api/oauth2/authorize?client_id=992797622094016622&permissions=8&scope=bot',description ="There are no banned users for this guild", color=0x2f3136)
        embed2.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}')
        await ctx.send(embed = embed2)

    @commands.command(aliases=['sb'])
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def softban(self, ctx, member: discord.Member, *, reason=None):
        """Soft bans a member from the server.
        A softban is basically banning the member from the server but
        then unbanning the member as well. This allows you to essentially
        kick the member while removing their messages.
        In order for this to work, the bot must have Ban Members permissions.
        To use this command, you must have Ban Members permission.
        """

        if reason is None:
            reason = f"$ No reason given.\nBanned by {ctx.author}"

        await member.bsn(reason=reason)
        await member.unban(reason=reason)
        await ctx.send(f"$ Sucessfully soft-banned {member}.")

    @commands.command()
   # @commands.has_permissions(m_messages=True)
    #@commands.bot_has_permissions(send_messages=True)
    async def vclist(self,ctx):
        ''' Get the list of members in vc you are connected to'''
        if not ctx.message.author.voice:
            await ctx.send(f" | You are not connected to any voice channels")
        else:
            member_list = ctx.message.author.voice.channel.members
            color = await self.fetch_color(ctx)
            await lister(ctx,your_list=member_list,color=color,title=f"List of members in {ctx.message.author.voice.channel.name}")

  

    @commands.command(aliases=['tb'])
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tempban(self, ctx, member: discord.Member, time, d, *, reason="No Reason"):
      if member == None:
        embed = discord.Embed(f"<:hajaks:989006655511478294> | {ctx.message.author}, Please enter a valid user!")
        await ctx.reply(embed=embed)
      else:
        guild = ctx.guild
        embed = discord.Embed(title="Temporarily banned", description=f"<:sowlbz:989006711920668703> | {member.mention} has been temporarily banned!", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Reason: ", value=reason, inline=False)
        embed.add_field(name="Time left for the ban:", value=f"{time}{d}", inline=False)
        await ctx.reply(embed=embed)
        await guild.ban(user=member)
        
        if d == "s":
          await asyncio.sleep(int(time))
          await guild.unban(user=member)
          if d == "m":
            await asyncio.sleep(int(time*60))
            await guild.unban(user=member)
            if d == "h":
              await asyncio.sleep(int(time*60*60))
              await guild.unban(user=member)
              if d == "d":
                await asyncio.sleep(time*60*60*24)
                await guild.unban(int(user=member))

    @commands.group(invoke_without_command=True)
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self, ctx,amount:int=10):
        if amount >1000:
            return await ctx.send("<:hajaks:989006655511478294> | Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        deleted = await ctx.channel.purge(limit=amount+1)
        return await ctx.send(f"<:sowlbz:989006711920668703> | deleted {len(deleted)-1} message(s)")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def startswith(self, ctx, key, amount: int = 10):
        if amount >1000:
            return await ctx.send("<:hajaks:989006655511478294> | Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.content.startswith(key):
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"<:sowlbz:989006711920668703> | deleted {len(deleted)}/{amount} message(s) which started with the given keyword")


    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def endswith(self, ctx, key, amount: int = 10):
        if amount >1000:
            return await ctx.send("<:hajaks:989006655511478294> | Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.content.endswith(key):
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"<:sowlbz:989006711920668703>| deleted {len(deleted)}/{amount} message(s) which ended with the given keyword")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def contains(self, ctx, key, amount: int = 10):
        if amount >1000:
            return await ctx.send("<:hajaks:989006655511478294> | Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if key in m.content:
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"<:sowlbz:989006711920668703> | deleted {len(deleted)}/{amount} message(s) which contained the given keyword")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def user(self, ctx, user: discord.Member, amount: int = 10):
        if amount >1000:
            return await ctx.send("<:hajaks:989006655511478294> | Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.author.id == user.id:
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"<:sowlbz:989006711920668703> | deleted {len(deleted)}/{amount} message(s) which were sent by the mentioned user")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def invites(self, ctx, amount: int = 10):
        if amount >1000:
            return await ctx.send("<:hajaks:989006655511478294> | Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if "discord.gg/" in m.content.lower():
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"<:sowlbz:989006711920668703> | deleted {len(deleted)}/{amount} message(s) which contained invites")

# TODO: add proper cooldowns to all the commands listed here
# TODO ability to 
#@commands.has_permissions(send_messages=True)
    @commands.command(aliases=["list-bots"])
  #@commands.bot_has_permissions(send_messages=True)
    async def _bots(self,ctx):
        ''' Lists the bots in your server '''
        bots_list = []
        for m in ctx.guild.members:
            if m.bot:
                bots_list.append(m)
        color = 0x2f3136
        await lister(ctx,your_list=bots_list,color=color,title=f"<:sowlbz:989006711920668703> | List of bots in {ctx.guild.name}")
      
    @commands.command(aliases=['m'])
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx: commands.Context, member: discord.Member, *, reason="No Reason Provided."):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        if ctx.author.top_role.position > member.top_role.position or ctx.author == guild.owner:
            await ctx.send(f"<:sowlbz:989006711920668703> | Successfully muted {member.display_name}")
            await member.add_roles(mutedRole, reason=reason)
            await member.send(f":exclamation: | You have been muted from: {guild.name} reason: {reason}")
        if not ctx.author.top_role.position > member.top_role.position and ctx.author != ctx.guild.owner:
            await ctx.send(f"<:cross_no:983596856242233384> | You cannot mute someone with a higher role than you!")

    @commands.command(aliases=['mutehoja'])
    @commands.guild_only()
    @commands.has_permissions(moderate_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def timeout(self, ctx, member: discord.Member, duration, *, reason=None):
        """
        Mutes or timeouts a member for specific time.
        Maximum duration of timeout: 28 days (API limitation)
        Use 5m for 5 mins, 1h for 1 hour etc...
        In order for this to work, the bot must have Moderate Members permissions.
        To use this command, you must have Moderate Members permission.
        """

        if reason is None:
            reason = f"Action done by {ctx.author}"

        humanly_duration = humanfriendly.parse_timespan(duration)

        await member.timeout(
            discord.utils.utcnow() + datetime.timedelta(seconds=humanly_duration),
            reason=reason
        )
        await ctx.send(f"<:sowlbz:989006711920668703> | {self.bot.yes} {member} has been timed out for {duration}.\nReason: {reason}")

    @commands.command(aliases=['unm'])
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await ctx.send(f"<:sowlbz:989006711920668703> | {member.display_name} has been unmuted")
        await member.remove_roles(mutedRole)
        await member.send(f":exclamation: | You are have been unmuted from: {ctx.guild.name}")



    @commands.command(aliases=['k'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason=None):
        if member == self.bot:
            await ctx.send(f"<:hajaks:989006655511478294> | You cannot kick me!")
        if ctx.author.top_role.position > member.top_role.position or member == ctx.guild.owner:
            await member.kick(reason=reason)
            await ctx.send(f"<:sowlbz:989006711920668703> | {member.display_name} has been kicked from this guild, for: {reason}")
            await member.send(f":exclamation: | You have been kicked from {ctx.guild.name} for: {reason}!")
        if not ctx.author.top_role.position > member.top_role.position and ctx.author != ctx.guild.owner:
            await ctx.send(f"<:hajaks:989006655511478294> | You cannot kick someone with a higher role than you!")

    @commands.command()
    async def enlarge(self, ctx, emoji: discord.Emoji):
        ''' Enlarge any emoji '''
        # url = ctx.emoji.url_as(self,format='png')
        url = emoji.url
        await ctx.send(url)
      
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def roleallhumans(self,ctx,role:discord.Role):
        ''' Gives all the humans any role '''
        humans = [mem for mem in ctx.guild.members if not mem.bot]
        await ctx.send("<:sowlbz:989006711920668703> | Adding roles to all humans")
        for h in humans:
            await h.add_roles(role)
        await ctx.reply('<:sowlbz:989006711920668703> | Added mentioned role to all members')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def roleallbots(self,ctx,role:discord.Role):
        ''' Give all bots any role '''
        humans = [mem for mem in ctx.guild.members if mem.bot]
        await ctx.send("<:sowlbz:989006711920668703> | Adding roles to all humans & bots")
        for h in humans:
            await h.add_roles(role)
        await ctx.reply('<:sowlbz:989006711920668703> | Added mentioned role to all bots')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def removeallhumans(self,ctx,role:discord.Role):
        ''' Removes a role from all human members '''
        humans = [mem for mem in ctx.guild.members if not mem.bot]
        await ctx.send("<:sowlbz:989006711920668703> | Removing roles from all humans")
        for h in humans:
            await h.remove_roles(role)
        await ctx.reply('<:sowlbz:989006711920668703> | Removed mentioned role from all members')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def removeallbots(self,ctx,role:discord.Role):
        ''' Removes a role from all the bots '''
        humans = [mem for mem in ctx.guild.members if mem.bot]
        await ctx.send("<:sowlbz:989006711920668703> | Removing roles to all humans & bots")
        for h in humans:
            await h.remove_roles(role)
        await ctx.reply('<:sowlbz:989006711920668703> | Removed mentioned role from all bots')

  
    @commands.command(aliases=['w'])
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member, * , reason="No Reason Provided!"):
        await ctx.send(f"<:sowlbz:989006711920668703> | {member.display_name} has been warned for: {reason}")
        await member.send(f":exclamation: | You have been warned in {ctx.guild.name} for: {reason}")



                   


    @commands.command()
    async def vcdeafen(self, ctx, user: discord.Member, * , reason=None):
        await ctx.send(f"<:sowlbz:989006711920668703> | {user.display_name} has been deafened, for: {reason}")
        await user.edit(deafen = True)

    @commands.command(aliases=["vCmute"])
    async def vcmute(self, ctx, member: discord.Member, * , reason=None):
        await ctx.send(f"<:sowlbz:989006711920668703> | {member.display_name} has been muted, for: {reason}")
        await member.edit(mute = True)

    @commands.command()
    async def vcunmute(self, ctx, member: discord.Member):
        await ctx.send(f"<:sowlbz:989006711920668703> | {member.display_name} has been unmuted.")
        await member.edit(mute = False)

    @commands.command()
    async def vcundeafen(self, ctx, member: discord.Member):
        await ctx.send(f"<:sowlbz:989006711920668703> | {member.display_name} has been undeafened.")
        await member.edit(deafen = False)

    @commands.command()
    @commands.has_permissions(manage_emojis=True)
    async def delemoji(self, ctx, emoji: discord.Emoji):
        await emoji.delete()
        await ctx.send(f"<:sowlbz:989006711920668703> | emoji has been deleted.")

 


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, member: discord.Member, *, reason=None):
        if member == self.bot:
            await ctx.send('<:hajaks:989006655511478294> | You cannot ban the bot!')
        if ctx.author.top_role.position > member.top_role.position or ctx.author == ctx.guild.owner:
            await member.ban(reason=reason)
            await ctx.send(f"<:sowlbz:989006711920668703> | {member.display_name} has been successfully banned")
            await member.send(f":exclamation: | You have been banned from {ctx.message.guild.name} for reason: {reason}")
        if not ctx.author.top_role.position > member.top_role.position and ctx.author != ctx.guild.owner:
            await ctx.send(f"<:hajaks:989006655511478294> | You cannot ban someone with a higher role than you.")


    @commands.command()
  	#@commands.has_permissions(kick_members=True)
    async def block(self, ctx, user):
        """
        Blocks a user from chatting in current channel.
           
        Similar to mute but instead of restricting access
        to all channels it restricts in current channel.
        """
                                
        if not user: # checks if there is user
            return await ctx.send("You must specify a user")
                                
        await ctx.set_permissions(user, send_messages=False) # sets permissions for current channel
    
    @commands.command()
  	#@commands.has_permissions(kick_members=True)
    async def unblock(self, ctx, user):
        """Unblocks a user from current channel"""
                                
        if not user: # checks if there is user
            return await ctx.send("You must specify a user")
        
        await ctx.set_permissions(user, send_messages=True) # gives back send messages permissions


    
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id: int):
        user = await self.bot.fetch_user(id)
        await ctx.guild.unban(user)
        await ctx.send(f"<:sowlbz:989006711920668703> | {user.name} has been successfully unbanned")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def clone(self, ctx, channel: discord.TextChannel):
        await channel.clone()
        await ctx.send(f"<:sowlbz:989006711920668703> | {channel.name} has been successfully cloned")


    

def setup(bot):
    bot.add_cog(moderation(bot))