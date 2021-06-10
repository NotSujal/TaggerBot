import discord
from discord.ext import commands
import os
from pretty_help import DefaultMenu, PrettyHelp
from assist import *


client = commands.Bot(command_prefix=">",case_insensitive = True)

menu = DefaultMenu('◀️', '▶️', '❌')
client.help_command = PrettyHelp(navigation=menu, color= 0x00ffff)

"""
Not None Catagory
"""


@client.event
async def on_ready():
    print(f" Successfully Logged in ")

@client.command(aliases=["latency"])
async def ping (ctx):
    """
    Get the latest latency of the bot
    """
    await ctx.send(f"Pong!  {round( client.latency * 1000)}")

@client.command(aliases=['info'])
async def support(ctx):
    """
    Get the support link
    """



for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run(os.getenv('TOKEN'))
