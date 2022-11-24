import discord, json
from discord.ext import commands
from .utils.config import *
import motor.motor_asyncio as mongodb

class leave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.connection = mongodb.AsyncIOMotorClient("mongodb+srv://hacker:chetan2004@cluster0.rxh8r.mongodb.net/Flame?retryWrites=true&w=majority")
        self.db = self.connection["Zeon"]["servers"]

    @commands.group(name="leave", description="leave channel\leave config\leave delete", invoke_without_command=True)
    @commands.has_permissions(administrator=True)
    async def leave(self, ctx):
        """leave channel\leave config\leave delete"""
        x = "!"
        await ctx.send(f"Available Commands: `{x}leave channel`")

    @leave.command()
    @commands.has_permissions(administrator=True)
    async def channel(self, ctx, c: discord.TextChannel):
        try:
            await self.db.update_one(
                {
                    "guild": ctx.guild.id
                },
                {
                    "$set": {
                        "leave-channel" : c.id
                    }
                }
            )
            await ctx.send(f"<a:nr_tick:956867762398044200>  | leave channel are updated to <#{c.id}>")
        except Exception as e:
            return await ctx.send(f"An error occoured {e}")

    @leave.command(aliases=['show'])
    @commands.has_permissions(administrator=True)
    async def config(self, ctx):
        data = await self.db.find_one({"guild": ctx.guild.id})     
        x = data["leave-channel"]
        if x == None:
          embed = discord.Embed(title=f"leave channel:", description=f"No leave Channel Found", color = 0x2f3136)
          await ctx.send(embed=embed)
        else:
          embed = discord.Embed(title=f"leave channel:", description=f"<#{x}>", color = 0x2f3136)
          await ctx.send(embed=embed)

    @leave.command()
    @commands.has_permissions(administrator=True)
    async def delete(self, ctx: commands.Context):
        await self.db.update_one(
                {
                    "guild": ctx.guild.id
                },
                {
                    "$set": {
                        "leave-channel" : None
                    }
                }
            )
        await ctx.send(f'<a:nr_tick:956867762398044200> | Successfully Deleted Leave Channel')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.bot:
            return
        data = await self.db.find_one({"guild": member.guild.id})     
        x = data["leave-channel"]
        if x == None:
          return
        else:  
          channel = self.bot.get_channel(x)
          member1 = int(member.created_at.timestamp())
          embed = discord.Embed(title="A member is no longer in the server.", description=f"{member.name} | {member.id}", color = discord.Colour.dark_red())
          embed.set_thumbnail(url=member.avatar)
          embed.set_author(name=member.name, icon_url=member.avatar)
          embed.set_footer(text="LEFT", icon_url=self.bot.user.avatar)
          await channel.send(embed=embed)
          
def setup(bot):
    bot.add_cog(leave(bot))