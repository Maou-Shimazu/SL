from __future__ import annotations

import discord
from discord.ext import commands, menus
from bot import Bot


class CommandConverter(commands.Converter):
    async def convert(self, command: str) -> commands.Command:
        pass


class HelpMenu(menus.ListPageSource):
    __slots__ = {}

    def __init__(self, ctx: commands.Context, data: list[commands.Command]) -> None:
        self.ctx = ctx
        super().__init__(data, per_page=3)

    async def write_page(self, menu, fields: list[tuple[str, str]]) -> None:
        pass

    async def format_page(self, menu, entries: list[commands.Command]) -> None:
        pass


class Help(commands.Cog):
    __slots__ = {"bot"}

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.command(name="help", help="Shows this message.")
    async def command_help(self, cmd: commands.Command | None) -> None:
        if cmd:
            pass


def setup(bot: Bot) -> None:
    bot.add_cog(Help(bot))
