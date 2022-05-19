from pathlib import Path
import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands
from pytz import utc
import requests


class Bot(commands.Bot):
    __slots__ = ("ready", "extentions", "sheduler")

    def __init__(self) -> None:
        self.ready = False
        self.extentions = [p.stem for p in Path(".").parent.glob("**/*.py")]
        self.sheduler = AsyncIOScheduler(timezone=utc)

        super().__init__(
            command_prefix="!!",
            status=discord.Status.online,
            intents=discord.Intents.all(),
            case_insensitive=True
        )

    def setup(self) -> None:
        print("Running setup...")
        for ext in self.extentions:
            self.load_extension(f"extentions.{ext}")
            print(f"`{ext}` loaded.")

    def run(self) -> None:
        self.setup()
        print("Running bot...")
        with open("token", "r") as f:
            token = f.read()
        super().run(token, reconnect=True)

    async def close(self) -> None:
        await super().close()

    async def on_connect(self) -> None:
        print(f"Bot Connected! DWSP Latency: {self.latency * 100:,.0f} ms")

    async def on_disconnect(self) -> None:
        print(f"Bot Disconnected.")

    async def on_ready(self) -> None:
        if not self.ready:
            return

        self.sheduler.start()
        self.guilds = self.get_guild(844329823655690270)

        print("Logged in as {0.user}".format(self))
        await self.change_presence(activity=discord.Activity(
            name="!!help", type=discord.ActivityType.listening))
        self.ready = True

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



    
