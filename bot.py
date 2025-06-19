import discord
from discord.ext import commands
import os
import logging
import asyncio
import config.environment_variables_config as environment_variables_config


logger = logging.getLogger(__name__)

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
intents.members = True  # Enable members intent if needed
intents.guilds = True  # Enable guilds intent


bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    await bot.change_presence(activity=discord.Game(name="Pigger is on duty!"))
    await bot.tree.sync()

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(environment_variables_config.TOKEN)

asyncio.run(main())