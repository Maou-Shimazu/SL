import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging

intents = discord.Intents.default()
intents.members = True

logging.basicConfig(level=logging.INFO)
load_dotenv()
tok = os.getenv('tok')

activity = discord.Activity(name='~help', type=discord.ActivityType.listening)
client = commands.Bot(command_prefix='~', intents=intents, activity=activity)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def welcome(ctx):
    embedVar = discord.Embed(title="Welcome!", description=f"Welcome To Shimazu Clan, **{ctx.author.name}**",color=0x00ff00)
    embedVar.set_thumbnail(url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=embedVar)

@client.event
async def on_member_join(member):
    print(f'{member} Joined the server!')
    embedVar = discord.Embed(title="Welcome!", description=f"Welcome To Shimazu Clan, **{member}**",color=0x00ff00)
    embedVar.set_thumbnail(url=f"{member.avatar_url}")
    #channel = discord.utils.get(member.guild.text_channels, name="general")
    channel = client.get_channel(878110758867705976)
    await channel.send(embed=embedVar)
    #await channel.send('hello')

client.run(tok)
