import discord
from discord.ext import commands
from bot import Bot

MAOU_ID = 859581812246446081
R_ID = "977742294432231454"

class Qt(commands.Cog):
    __slots_ = {"bot", }

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        await payload.message.add_reaction(R_ID)
async def setup(bot: Bot):
    bot.add_cog(Qt(bot))