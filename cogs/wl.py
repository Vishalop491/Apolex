import discord
from discord.ext import commands
from Helpers.data import getConfig, updateConfig
import asyncio
import json
from itertools import cycle

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}


class wl(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(usage="<member>",
                      name="whitelist",
                      description="Adds member to the server whitelist")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 1, commands.BucketType.member)
    @commands.guild_only()
    async def whitelist(self, ctx, member: discord.Member = None):
        try:
            data = getConfig(ctx.guild.id)
            if ctx.author.id == ctx.guild.owner_id:
                if member == None:
                    embed = discord.Embed(title='Apolex', description=f'**`Please Specify A Member To Whitelist`**')
                    embed.set_author(
            name='Apolex',
            icon_url=            'https://images-ext-1.discordapp.net/external/cAtd1tILoERtU1SBq7qQIbfyXJMdtOoftjcjw7HoS8c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png'
                    )
                    embed.set_thumbnail(
            url=            'https://images-ext-1.discordapp.net/external/cAtd1tILoERtU1SBq7qQIbfyXJMdtOoftjcjw7HoS8c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png'
        )
                    await ctx.send(embed=embed)
                else:
                    data = getConfig(ctx.guild.id)
                    whitelisted = data["whitelist"]
                    if member.id in whitelisted:
                      embed = discord.Embed(title='Apolex', description=f'**`User is already in Whitelist!`**')
                      embed.set_author(
            name='Apolex',
            icon_url=            'https://images-ext-1.discordapp.net/external/cAtd1tILoERtU1SBq7qQIbfyXJMdtOoftjcjw7HoS8c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png'
                    )
                      embed.set_thumbnail(
            url=            'https://images-ext-1.discordapp.net/external/cAtd1tILoERtU1SBq7qQIbfyXJMdtOoftjcjw7HoS8c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png'
        )
                      return await ctx.send(embed=embed)
                    else:
                        data = getConfig(ctx.guild.id)
                        data["whitelist"].append(member.id)
                        embed = discord.Embed(title='Apolex', description=f'<@{member.id}> `Has been added to Whitelist`')
                        embed.set_author(
            name='Apolex',
            icon_url=            'https://images-ext-1.discordapp.net/external/cAtd1tILoERtU1SBq7qQIbfyXJMdtOoftjcjw7HoS8c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png'
                    )
                        embed.set_thumbnail(
            url=            'https://images-ext-1.discordapp.net/external/cAtd1tILoERtU1SBq7qQIbfyXJMdtOoftjcjw7HoS8c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png'
        )
                        await ctx.send(embed=embed)
                        updateConfig(ctx.guild.id, data)
            else:
                embed = discord.Embed(title='Apolex', description=f'<@{ctx.guild.owner.id}> `Only Guild Owner can whitelist users`')
                embed.set_author(
            name='Apolex',
            icon_url=            'https://images-ext-1.discordapp.net/external/cAtd1tILoERtU1SBq7qQIbfyXJMdtOoftjcjw7HoS8c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png'
        )
                embed.set_thumbnail(
            url=            'https://images-ext-1.discordapp.net/external/cAtd1tILoERtU1SBq7qQIbfyXJMdtOoftjcjw7HoS8c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png'
        )
                await ctx.send(embed=embed)
        except:
            pass

    @commands.command(usage="<member>",
                      name="unwhitelist",
                      description="Removes member from the server whitelist")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 1, commands.BucketType.member)
    @commands.guild_only()
    async def unwhitelist(self, ctx, member: discord.Member = None):
        try:
            data = getConfig(ctx.guild.id)
            if ctx.author.id == ctx.guild.owner_id:
                if member == None:
                    embed = discord.Embed(title='Apolex', description=f'**`Please Specify A Member To Unwhitelist`**')
                    embed.set_author(
            name='Apolex',
            icon_url=            'https://images-ext-1.discordapp.net/external/cAtd1tILoERtU1SBq7qQIbfyXJMdtOoftjcjw7HoS8c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png'
                    )
                    embed.set_thumbnail(
            url=            'https://images-ext-1.discordapp.net/external/cAtd1tILoERtU1SBq7qQIbfyXJMdtOoftjcjw7HoS8c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png'
        )
                    await ctx.send(embed=embed)
                else:
                    data = getConfig(ctx.guild.id)
                    whitelisted = data["whitelist"]
                    if member.id not in whitelisted:
                      embed = discord.Embed(title='Apolex', description=f'**`User is not Whitelisted!`**')
                      embed.set_author(
            name='Apolex',
            icon_url=            'https://images-ext-1.discordapp.net/external/cAtd1tILoERtU1SBq7qQIbfyXJMdtOoftjcjw7HoS8c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png'
                    )
                      embed.set_thumbnail(
            url=            'https://images-ext-1.discordapp.net/external/cAtd1tILoERtU1SBq7qQIbfyXJMdtOoftjcjw7HoS8c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png'
        )
                      return await ctx.send(embed=embed)
                    else:
                        data = getConfig(ctx.guild.id)
                        data["whitelist"].append(member.id)
                        embed = discord.Embed(title='Apolex', description=f'<@{member.id}> `Has been  Unwhitelisted`')
                        embed.set_author(
            name='Apolex',
            icon_url=            'https://images-ext-1.discordapp.net/external/cAtd1tILoERtU1SBq7qQIbfyXJMdtOoftjcjw7HoS8c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png'
                    )
                        embed.set_thumbnail(
            url=            'https://images-ext-1.discordapp.net/external/cAtd1tILoERtU1SBq7qQIbfyXJMdtOoftjcjw7HoS8c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png'
        )
                        await ctx.send(embed=embed)
                        updateConfig(ctx.guild.id, data)
            else:
                embed = discord.Embed(title='Apolex', description=f'<@{ctx.guild.owner.id}> `Only Guild Owner can Unwhitelist users`')
                embed.set_author(
            name='Apolex',
            icon_url=            'https://images-ext-1.discordapp.net/external/cAtd1tILoERtU1SBq7qQIbfyXJMdtOoftjcjw7HoS8c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png'
        )
                embed.set_thumbnail(
            url=            'https://images-ext-1.discordapp.net/external/cAtd1tILoERtU1SBq7qQIbfyXJMdtOoftjcjw7HoS8c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png'
        )
                await ctx.send(embed=embed)
        except:
            pass

    @commands.command(name="whitelisted",
                      description="Shows you the current server whitelist")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 1, commands.BucketType.member)
    @commands.guild_only()
    async def whitelisted(self, ctx):
        prefix = "!"
        try:
            data = getConfig(ctx.guild.id)
            whitelisted = data["whitelist"]
            if ctx.author.id in whitelisted or ctx.author.id == ctx.guild.owner_id:
                loading = await ctx.send("Searching...")
                result = ' '
                data = getConfig(ctx.guild.id)
                userinwhitelist = data["whitelist"]
                for i in userinwhitelist:
                    user2 = self.client.get_user(i)
                    if user2 == None:
                        user = 'Unable to Fetch Name'
                    else:
                        user = user2.mention
                    result += f"{user}: {i}\n"
                await loading.delete()
                if data["whitelist"] == []:
                    return await ctx.send(f"There are no whitelisted users in this server, do `{prefix}whitelist <user>` to whitelist a user of your choice!")
                else:
                    embed = discord.Embed(title=f'Whitelisted users for {ctx.guild.name}', description=result)
                    await ctx.send(embed=embed)

            else:
                embed = discord.Embed(title='Apolex', description=f'<@{ctx.guild.owner.id}> `Only Guild Owner or a whitelisted user can see whitelist!`')
                embed.set_author(
            name='Apolex',
            icon_url=            'https://images-ext-1.discordapp.net/external/cAtd1tILoERtU1SBq7qQIbfyXJMdtOoftjcjw7HoS8c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png'
        )
                embed.set_thumbnail(
            url=            'https://images-ext-1.discordapp.net/external/cAtd1tILoERtU1SBq7qQIbfyXJMdtOoftjcjw7HoS8c/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/992797622094016622/e257d7dcfe64528df19b8dfe37b539f4.png'
        )
                await ctx.send(embed=embed)
        except:
            pass

def setup(client):
    client.add_cog(wl(client))            