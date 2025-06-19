from discord.ext import commands
from services.cs2_service import cs2_weekly_reset_countdown
import logging

logger = logging.getLogger(__name__)

class CS2(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f'{self.__class__.__name__} is ready!')

    @commands.hybrid_command()
    async def cs2_drop(self, ctx):
        try:
            time = cs2_weekly_reset_countdown()
            await ctx.send(f"{ctx.author.mention}, {time}")
            logger.debug(f"Sent CS2 drop time to {ctx.author}")
        except Exception as e:
            logger.error("Error in cs2_drop command", exc_info=True)
            await ctx.send("Something went wrong fetching the CS2 drop time.")

async def setup(bot: commands.Bot):
    await bot.add_cog(CS2(bot))
    logger.info(f'{__name__} cog loaded successfully!')