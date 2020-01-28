import discord
import asyncio
from discord.ext import tasks, commands

class dmlistener(commands.Cog):
    def __init__(self, bot, channelid, chatbot):
        self.bot = bot
        self.channelid = channelid
        self.chatbot = chatbot

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.channel.id == self.channelid:
            return
        if message.author.bot:
            return    
            
        await message.channel.send(self.chatbot.message(message.content))

    @commands.command()
    async def start(self):
        await self.bot.get_channel(self.channelid).send(self.chatbot.init())