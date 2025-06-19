from discord.ext import commands
from services.cs2_service import cs2_weekly_reset_countdown
import logging


logger = logging.getLogger(__name__)

class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f'{self.__class__.__name__} is ready!')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send(
        f"Welcome to the server, {member.name}! If you have any questions, feel free to ask."
    )
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if "oe" in message.content.lower():
            await message.channel.send(
                f"{message.author.mention}, anan oe."
            )

        # Process commands if any
        await self.bot.process_commands(message)

    @commands.hybrid_command()
    async def hello(self, ctx):
        logger.info(f"hello command triggered by {ctx.author} in #{ctx.channel}")
        await ctx.send(f"Hello, {ctx.author.mention}! How can I assist you today?")

    @commands.hybrid_command()
    async def dm(self, ctx, *, msg):
        try:
            await ctx.author.send(f"Direct Message: {msg}")
            logger.info(f"dm command sent to {ctx.author}: {msg}")
        except Exception as e:
            logger.error(f"Failed to DM {ctx.author}: {e}", exc_info=True)
            await ctx.send("I couldn't send you a DM. Please check your privacy settings.")

async def setup(bot: commands.Bot):
    await bot.add_cog(General(bot))
    logger.info(f'{__name__} cog loaded successfully!')