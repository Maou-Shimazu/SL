import discord
from discord.ext import commands
from bot import Bot


class Comms(commands.Bot):
    __slots__ = {"bot"}

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.Bot.command()
    async def test(self):
        print("This actually works.")

    @commands.Bot.command()
    async def pet(ctx, member: discord.Member = None):
        if member is None:
            await ctx.send(f"https://pfpet.herokuapp.com/d/{ctx.author.id}.gif")
        else:
            await ctx.send(f"https://pfpet.herokuapp.com/d/{member.id}.gif")

    @commands.Bot.command()
    async def bonk(ctx, member: discord.Member = None):
        if member is None:
            await ctx.send(f"https://pfpet.herokuapp.com/d/bonk/{ctx.author.id}.gif")
        else:
            await ctx.send(f"https://pfpet.herokuapp.com/d/bonk/{member.id}.gif")


def setup(bot: Bot) -> None:
    bot.add_command(Comms(bot))
