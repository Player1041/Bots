import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import os


load_dotenv()

token = os.environ["token"]

bot = commands.Bot(
    intents = disnake.Intents.all(),
    test_guilds = [951289542684590140],
    reload = True)

bot.load_extensions("commands")

@bot.event
async def on_ready():
    print("Loaded GameStats!")

bot.run(token)