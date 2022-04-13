import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import os


load_dotenv()

token = os.environ["token"]

bot = commands.Bot(
    intents = disnake.Intents.all(),
    reload = True,
    test_guilds = [951289542684590140])
    
bot.load_extensions("commands")

@bot.event
async def on_ready():
    print("Loaded YAMB.")

bot.run(token)