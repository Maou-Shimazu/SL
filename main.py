import os
import discord
import logging
import psycopg2
import requests
from typing import Optional
from dotenv import load_dotenv
from discord.ext import commands
import views

# Postgre connection to the SL database
connection = psycopg2.connect(user="sl",
                              password="sl",
                              host="127.0.0.1",
                              port="5432",
                              database="sl")

cursor = connection.cursor() # db cursor

# tags = '''
#         DROP TABLE IF EXISTS tags;
#         CREATE TABLE tags(
#             id      serial PRIMARY Key,
#             tag     text NOT NULL
#         ); '''
# cursor.execute(tags)
# connection.commit()
# print("Table tags created successfully in PostgreSQL ")
print("Connected to PostgreSQL")

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.messages = True
  
logging.basicConfig(level=logging.INFO)
load_dotenv()
tok = os.getenv('tok')
f = os.getenv('f')
prefixes: tuple = ("!s ", "!!")
activity = discord.Activity(
    name='!! help', type=discord.ActivityType.listening)
#commands.when_mentioned_or('!s ')
client = commands.Bot(command_prefix=commands.when_mentioned_or(*prefixes), intents=discord.Intents.default(), activity=activity)
client.case_insensitive = True
#client.remove_command('help')

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.command()
async def _help(ctx):
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
    print("saving content")
    for channel in ctx.guild.text_channels:
        async for message in channel.history(limit=1000):
            for attachment in message.attachments:
                if not os.path.exists(f"content/{channel}"):
                    os.mkdir(f"content/{channel}")
                await attachment.save(f"content/{channel}/" + attachment.filename)
    print("Saved content!")

#@client.command()
async def save_f(ctx):
    channel = discord.utils.get(ctx.guild.channels, name=f)
    async for message in channel.history(limit=200):
        if message.content.startswith('https://'):
            os.system(f"curl {message.content} --output content/{message.id}.png")
        for attachment in message.attachments:
            await attachment.save(f"content/" + attachment.filename)
    print("Saved content!")

@client.command()
async def add_tag(ctx, *, ttag = None):
    if ttag == "help":
        await ctx.send("To add a command use the syntax `!sl add_tag <tag>`.")
    elif ttag is not None:
        new_tag = f'''
        INSERT INTO tags(tag)
        VALUES ('{ttag}'); 
        '''
        cursor.execute(new_tag)
        connection.commit()
        await ctx.send(f"Added {ttag} into database!")
    else:
        await ctx.send("Please add a tag!")

@client.command()
async def remove_tag(ctx, *, ttag = None):
    if ttag is not None:
        new_tag = f'''
        DELETE FROM tags
        WHERE tag='{ttag}'; 
        '''
        cursor.execute(new_tag)
        connection.commit()
        await ctx.send(f"Removed {ttag} from database!")
    else:
        await ctx.send("Please add a tag to remove!")

@client.command()
async def get_tags(ctx, *, ttag = None):
    #await ctx.send("Tag command.")
    if ttag is None:
        get_tag = f'''
        SELECT tag from tags; 
        '''
        cursor.execute(get_tag)
        result = cursor.fetchall()
        r = ""
        for i in result:
            r += i[0] + ", "
        connection.commit()
        await ctx.send(f"Queried {r}from database!")
    #else:
        #await ctx.send("Please add a tag!")

@client.command()
async def timeout_example(ctx):
    """An example to showcase disabling buttons on timing out"""
    view = views.MyView()
    # Step 1
    view.message = await ctx.send('Press me!', view=view)

@client.command()
async def invite(ctx: commands.Context):
    await ctx.send(f'Invite link!', view=views.Invite())

client.run(tok)

if(connection):
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
