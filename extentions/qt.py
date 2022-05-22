import discord
from discord.ext import commands
from bot import Bot

MAOU_ID = 859581812246446081
R_ID = "<:oke:879424724332073020>"

class Qt(commands.Cog):
    __slots_ = {"bot"}

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent) -> None:
        message = await self.bot.guild.get_channel(payload.channel_id).fetch_message(payload.message_id)
        await message.add_reaction(R_ID)

    # @commands.Cog.listener()
    # async def on_message(self, message: discord.Message):
    #     await message.add_reaction(R_ID)


def setup(bot: Bot):
    bot.add_cog(Qt(bot))