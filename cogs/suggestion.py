import discord
import requests
from discord.ext import commands
from discord.ext.commands import BucketType, cooldown


class Suggestion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Suggestion cog loaded successfully")

    @commands.command()
    #@cooldown(1, 7200, BucketType.user)
    async def suggest(self, ctx, *, msg):
        channel = self.bot.get_channel(1002456585169281034)
        up = "\U0001f44d"
        down = "\U0001f44e"

        embed = discord.Embed(
            timestamp=ctx.message.created_at, title=f"Suggestion By {ctx.author}"
        )
        embed.add_field(name="Suggestion", value=msg)
        embed.set_footer(
            text=f"Wait until your suggestion is approved",
            icon_url=f"{ctx.author.avatar.url}",
        )
        message = await channel.send(embed=embed)
        await message.add_reaction(up)
        await message.add_reaction(down)
        await ctx.message.delete()
        await ctx.send("**Your Suggestion Has Been Recorded**")


def setup(bot):
    bot.add_cog(Suggestion(bot))