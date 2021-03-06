# starter.py
import os
import random
import discord
from discord.ext import commands
from bot.adder import Adder
from bot.game import Game
from bot.starter import StarterHelper
from dotenv import load_dotenv


intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.guilds = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!', intents=intents)
gameHelper = StarterHelper()

bot.add_cog(Game(bot, gameHelper))
bot.add_cog(Adder(bot))

bot.run(TOKEN)


