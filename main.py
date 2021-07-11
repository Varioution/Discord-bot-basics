import discord
import random
import os
from discord.ext import commands, tasks
from discord.ext import commands
from discord.ext.commands import Bot






client = discord.Client()


client = commands.Bot(command_prefix = '!')







@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))



@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('hello'):
    await message.channel.send('Hello!')
  


client.run("") #set your token here


