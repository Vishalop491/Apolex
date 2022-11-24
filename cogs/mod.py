import discord
from discord.ext import commands
import datetime

class mod(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_message(self, message):
        word_list = ['haoqlzjqpzbapzhqo']



        messageContent = message.content
        if len(messageContent) > 0:
            for word in word_list:
                if word in messageContent:
                    await message.delete()
                    await message.channel.send('Dont say this in chat')
            
        messageattachments = message.attachments
        if len(messageattachments) > 0:
            for attachment in messageattachments:
                if attachment.filename.endswith(".dll"):
                    await message.delete()
                    await message.channel.send("No DLL's allowed in chat!")
                elif attachment.filename.endswith('.exe'):
                    await message.delete()
                    await message.channel.send("No EXE's allowed in chat!")
                elif attachment.filename.endswith('.zip'):
                    await message.delete()
                    await message.channel.send("No ZIP's allowed in chat!")                   
                elif attachment.filename.endswith('.rar'):
                    await message.delete()
                    await message.channel.send("No RAR's allowed in chat!")                   
                elif attachment.filename.endswith('.flp'):
                    await message.delete()
                    await message.channel.send("No FLP's allowed in chat!")                  
                else:
                    break



def setup(client):
    client.add_cog(mod(client))          