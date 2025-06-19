import discord
from discord.ext import commands
from discord import app_commands
import logging
from services.role_service import get_assignable_roles, get_removable_roles


logger = logging.getLogger(__name__)

class Roles(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f'{self.__class__.__name__} is ready!')

    @commands.hybrid_command(name="assign", description="Assign a role to yourself.")
    @app_commands.autocomplete(role=get_assignable_roles)
    async def assign(self, ctx: commands.Context, role: str):
        role = discord.utils.get(ctx.guild.roles, name=role)
        if role:
            await ctx.author.add_roles(role)
            await ctx.send(f"{ctx.author.mention}, you have been assigned the **{role}** role.")
            logger.info(f"{ctx.author} assigned role: {role}")
        else:
            await ctx.send(f"{ctx.author.mention}, the **{role}** role does not exist.")
            logger.warning(f"{ctx.author} tried to assign nonexistent role: {role}")

    @commands.hybrid_command(name="remove", description="Remove a role from yourself.")
    @app_commands.autocomplete(role=get_removable_roles)
    async def remove(self, ctx: commands.Context, role: str):
        role = discord.utils.get(ctx.guild.roles, name=role)
        if role and role in ctx.author.roles:
            await ctx.author.remove_roles(role)
            await ctx.send(f"{ctx.author.mention}, you have been removed from the **{role}** role.")
            logger.info(f"{ctx.author} removed from role: {role}")
        elif role:
            await ctx.send(f"{ctx.author.mention}, you don't have the **{role}** role.")
            logger.warning(f"{ctx.author} tried to remove a role they don't have: {role}")
        else:
            await ctx.send(f"{ctx.author.mention}, the **{role}** role does not exist in this server.")
            logger.warning(f"{ctx.author} tried to remove nonexistent role: {role}")
    
    

async def setup(bot: commands.Bot):
    await bot.add_cog(Roles(bot))
    logger.info(f'{__name__} cog loaded successfully!')