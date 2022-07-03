from pathlib import Path
import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands
from pytz import utc
import requests

SHIMAZU_CLAN = 844329823655690270
BOT_SPAM_CHANNEL_ID = 844335549225762816

class Bot(commands.Bot):

    async def close(self) -> None:
        print("Shutting down...")
        self.scheduler.shutdown();
        await super().close()


    async def on_disconnect(self) -> None:
        print(f" Bot Disconnected.")

    async def on_ready(self) -> None:
        if self.ready:
            return

        self.guild = self.get_guild(SHIMAZU_CLAN)
        self.scheduler.start()
        print(f" Sheduler started ({len(self.scheduler.get_jobs()):,} job(s) scheduled)")
        print(" Logged in as {0.user}".format(self))
        self.ready = True
        print(f" Bot ready!")

    async def on_member_join(self, member):
        print(f'{member} Joined the server!')
        embed_var = discord.Embed(
            title="Welcome!",
            description=requests.get("https://sl-greeting-api.maou-shimazu.repl.co").headers["greeting"].replace(
                "<USER>", f"**{member.display_name}**"),
            color=0x00ff00
        )
        embed_var.set_thumbnail(url=f"{member.display_avatar}")
        channel = self.get_channel(878110758867705976)
        await channel.send(embed=embed_var)

    async def on_message(self, message: discord.Message, /) -> None:
        if message.author.bot or isinstance(message.channel, discord.DMChannel):
            return
        await self.process_commands(message)

    async def process_commands(self, message: discord.Message, /) -> None:
        ctx = await self.get_context(message, cls=commands.Context)
        if ctx.command is None:
            return
        await self.invoke(ctx)
