import os

import chatbot
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='eliza', help='Starts appointment with Eliza')
async def start(ctx, arg):
    response = chatbot.respond(arg)
    await ctx.send(response)

bot.run(token)

# make conversation last from "!eliza" to "!bye", set up virtual environment

# 3/28/20: Needed to reinstall textblob and discord.py