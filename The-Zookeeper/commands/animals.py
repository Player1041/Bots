import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv
import aiohttp
import json
import time
from enum import Enum
import random


load_dotenv()

cat_auth = os.environ["cat_auth"]
class AnimalsOptRand(str, Enum):
    Axolotl = "axolotl"
    Bunny = "bunny"
    Cat = "cat"
    Dog = "dog"
    Duck = "duck"
    Fox = "fox"
    Otter = "otter"
    Random = "random"

class AnimalsOpt(str, Enum):
    Axolotl = "axolotl"
    Bunny = "bunny"
    Cat = "cat"
    Dog = "dog"
    Duck = "duck"
    Fox = "fox"
    Otter = "otter"
    
class Animals(commands.Cog):
    """It's animal pics :)"""
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.slash_command()
    async def animals(self, inter, animal: AnimalsOptRand):
        """Displays an Animal photo."""
        if animal == "random":
            animal = random.choice(list(AnimalsOpt))
        if animal == "duck":
            async with aiohttp.ClientSession() as session:
                async with session.get("https://random-d.uk/api/v2/random") as resp:
                    data = json.loads(await resp.text())
                    duckEmbed = disnake.Embed(
                        title = "Duck!"
                    ).set_image(
                        url = data['url']
                    ).set_footer(
                        text = "Powered by Random Duck")
                    await inter.response.send_message(embed = duckEmbed)
        elif animal == "fox":
            async with aiohttp.ClientSession() as session:
                async with session.get("https://randomfox.ca/floof") as resp:
                    data = json.loads(await resp.text())
                    foxEmbed = disnake.Embed(
                        title = "Fox!"
                    ).set_image(
                        url = data['image']
                    ).set_footer(
                        text = "Powered by Random Fox")
                    await inter.response.send_message(embed = foxEmbed)
        elif animal == "axolotl":
            async with aiohttp.ClientSession() as session:
                async with session.get("http://axoltlapi.herokuapp.com") as resp:
                    data = await resp.json()
                    axoEmbed = disnake.Embed(
                        title = "Axolotl!"
                        ).set_image(
                            url = data["url"]
                        ).set_footer(
                            text = "Powered by the Axolotl API")
                    await inter.response.send_message(embed = axoEmbed)
        elif animal == "dog":
            async with aiohttp.ClientSession() as session:
                async with session.get("https://random.dog/woof.json") as resp:
                    data = json.loads(await resp.text())
                    dogEmbed = disnake.Embed(
                    title = "Dog!"
                    ).set_image(
                        url = data['url']
                    ).set_footer(
                        text = "Powered by Random Dog")
                    await inter.response.send_message(embed = dogEmbed)
        elif animal == "cat":
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://api.thecatapi.com/v1/images/search?api_key={cat_auth}") as resp:
                    data = json.loads(await resp.text())
                    catEmbed = disnake.Embed(
                    title = "Cat!"
                    ).set_image(
                        url = data[0]['url']
                    ).set_footer(
                        text = "Powered by The Cat API")
                    await inter.response.send_message(embed = catEmbed)
        elif animal == "bunny":
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.bunnies.io/v2/loop/random/?media=gif,png") as resp:
                    data = json.loads(await resp.text())
                    bunnyEmbed = disnake.Embed(
                    title = "Bunny!"
                    ).set_image(
                        url = data['media']['gif']
                    ).set_footer(
                        text = "Powered by bunnies.io")
                    await inter.response.send_message(embed = bunnyEmbed)
        elif animal == "otter":
            otterEmbed = disnake.Embed(
            title = "Otter!"
            ).set_image(
            url = f"https://otter-pics.up.railway.app/?huh={hash(time.time())}"
            ).set_footer(
            text = "Powered by Otter Photos API")
            await inter.response.send_message(embed = otterEmbed)

def setup(bot):
    bot.add_cog(Animals(bot))
    print("| Loaded Animals")