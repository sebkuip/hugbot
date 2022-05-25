import discord
from discord.ext import commands
import typing

from dotenv import load_dotenv
from os import getenv

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), help_command=None)

@bot.command(help="Give someone a big squeeze")
async def hug(ctx, member: typing.Optional[discord.User] = None) -> None:
    if member:
        embed = discord.Embed(description=f"{ctx.author} 🫂 {member}")
    else:
        embed = discord.Embed(description=f"{ctx.author} hugged themselves")

    await ctx.send(embed=embed)

load_dotenv(".env")
bot.run(getenv('TOKEN'))