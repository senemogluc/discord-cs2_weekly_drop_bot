import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import logging
from services.cs2_service import cs2_weekly_reset_countdown


# Load environment variables from .env file
load_dotenv()

try:
    TOKEN = os.getenv("DISCORD_TOKEN")
except:
    raise ValueError("DISCORD_TOKEN not found in environment variables. Please set it in the .env file.")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
intents.members = True  # Enable members intent if needed
intents.guilds = True  # Enable guilds intent


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')

@bot.event
async def on_member_join(member):
    await member.send(
        f"Welcome to the server, {member.name}! If you have any questions, feel free to ask."
    )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "oe" in message.content.lower():
        await message.channel.send(
            f"{message.author.mention}, anan oe."
        )

    # Process commands if any
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}! How can I assist you today?")

@bot.command()
async def assign(ctx, msg: str):
    role = discord.utils.get(ctx.guild.roles, name=msg)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention}, you have been assigned the {msg} role.")
    else:
        await ctx.send(f"{ctx.author.mention}, the {msg} role does not exist in this server.")

@bot.command()
async def remove(ctx, msg: str):
    role = discord.utils.get(ctx.guild.roles, name=msg)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention}, you have been removed from the {msg} role.")
    else:
        await ctx.send(f"{ctx.author.mention}, the {msg} role does not exist in this server.")

@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send(f"Direct Message: {msg}")

@bot.command()
async def test(ctx):
    time = cs2_weekly_reset_countdown()
    await ctx.send(f"{ctx.author.mention}, {time}")

bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)