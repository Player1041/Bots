import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv
import time

load_dotenv()

token = os.environ["token"]

bot = commands.Bot(
    intents = disnake.Intents.all(),
    test_guilds = [968232921913761934, 951289542684590140],
    reload = True)
    
bot.load_extensions("commands")

@bot.event
async def on_ready():
    print("Prepared for Adventure!")

bot.run(token)