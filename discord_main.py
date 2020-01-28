import discord
import Discord.token_manager
import Discord.dmlistener
from Discord.dmlistener import dmlistener
from discord.ext import commands
from Discord.token_manager import TOKEN as TOKEN


import Gollum.eliza
from Gollum.eliza import Eliza as Chatbot

channelID = 671840489540157462


cbot = Chatbot()
cbot.load('Gollum/doctor.txt')
bot = commands.Bot("g.", help_command = None)

dml = dmlistener(bot, channelID, cbot)
bot.add_cog(dml)

@bot.event
async def on_ready():
    print("Started!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" for stories"))

bot.run(TOKEN)
