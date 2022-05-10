import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging
import requests

intents = discord.Intents.default()
intents.members = True
intents.reactions = True

logging.basicConfig(level=logging.INFO)
load_dotenv()
tok = os.getenv('tok')
f = os.getenv('f')

activity = discord.Activity(
    name='!sl help', type=discord.ActivityType.listening)
client = commands.Bot(command_prefix='!sl ',
                      intents=intents, activity=activity)


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.command()
async def help_(ctx):
    embedVar = discord.Embed(
        title="**Commands!**", description=f"**The prefix is `!sl`, Add it before any command.**", color=0x00ff00)
    # embedVar.set_thumbnail(url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=embedVar)


@client.event
async def on_member_join(member):
    print(f'{member} Joined the server!')
    embedVar = discord.Embed(
        title="Welcome!",
        description=requests.get("https://random-hi.13-05.repl.co").headers["greeting"].replace(
            "<USER>", f"**{member}**".split("#", 1)[0] + "**"),
        color=0x00ff00
    )
    #description=f"Welcome To Shimazu Clan, **{member}**",
    embedVar.set_thumbnail(url=f"{member.avatar_url}")
    #channel = discord.utils.get(member.guild.text_channels, name="general")
    channel = client.get_channel(878110758867705976)
    await channel.send(embed=embedVar)


@client.command()
async def pet(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(f"https://pfpet.herokuapp.com/d/{ctx.author.id}.gif")
    else:
        await ctx.send(f"https://pfpet.herokuapp.com/d/{member.id}.gif")


@client.command()
async def bonk(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(f"https://pfpet.herokuapp.com/d/bonk/{ctx.author.id}.gif")
    else:
        await ctx.send(f"https://pfpet.herokuapp.com/d/bonk/{member.id}.gif")


@client.command()
async def save_content(ctx):
    for channel in ctx.guild.text_channels:
        async for message in channel.history(limit=200):
            for attachment in message.attachments:
                if not os.path.exists(f"content/{channel}"):
                    os.mkdir(f"content/{channel}")
                await attachment.save(f"content/{channel}/" + attachment.filename)
    print("Saved content!")

@client.command()
async def save_f(ctx):
    channel = discord.utils.get(ctx.guild.channels, name=f)
    async for message in channel.history(limit=200):
        if message.content.startswith('https://'):
            os.system(f"curl {message.content} --output content/{message.id}.png")
        for attachment in message.attachments:
            await attachment.save(f"content/" + attachment.filename)
    print("Saved content!")

client.run(tok)
