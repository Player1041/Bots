import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv
import platform

load_dotenv()

token = os.environ["token"]
split = ("----------------------")
indent = "| "
bot = commands.Bot(
    intents = disnake.Intents.all())

def loading():
	print(f"{indent}Bot stats:")
	print(f"{indent}Name: {bot.user}")
	print(f"{indent}ID: {bot.user.id}")
	print(f"{indent}Latency: {round(bot.latency * 1000)}ms")
	print(f"{indent}Disnake Version: {disnake.__version__}")
	print(f"{indent}Python Version: {platform.python_version()}")

bot.load_extensions("commands")

@bot.event
async def on_ready():
	loading()
bot.run(token)