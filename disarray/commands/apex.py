import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv
import aiohttp
import json
from enum import Enum

class Platform(Enum):
    PSN = "PS4"
    PC = "PC"
    XBOX = "X1"

Maps = commands.option_enum({
    "Arenas": "arenas",
    "Battle Royale": "battle_royale",
    "Ranked Arenas": "arenasRanked",
    "Ranked Battle Royale": "ranked"
})

load_dotenv()

apex_key = os.environ["apex_key"]

class Apex(commands.Cog):
    """A list of apex commands."""
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.slash_command()
    async def apex(self, inter):
        pass
    
    @apex.sub_command()
    async def stats(self, inter, platform: Platform, user: str):
        """Shows the stats of a given user.
        
        Parameters
        ----------
        
        platform: Select from PC, PSN or Xbox, there is no switch support due to API limitations.
        user: The username of the user to search"""

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.mozambiquehe.re/bridge?version=5&platform={platform}&player={user}&auth={apex_key}") as resp:
                data = json.loads(await resp.text())
                statsEmbed = disnake.Embed(
                    title = "Player Stats - Apex",
                    description = f"{data['global']['name']}'s info:",
                    colour = disnake.Colour.random()
                ).add_field(
                        name = "General:",
                        value = f"""UID - {data['global']['uid']}
                        \nLevel - {data['global']['level']}
                        """
                ).add_field(
                        name = "Ranks:",
                        value = f"""Battle Royale - {data['global']['rank']['rankName']} {data['global']['rank']['rankDiv']}
                        \nRP - {data['global']['rank']['rankScore']}
                        \nArena - {data['global']['arena']['rankName']} {data['global']['arena']['rankDiv']}
                        \nAP - {data['global']['arena']['rankScore']}""")
                await inter.response.send_message(embed = statsEmbed)


    @apex.sub_command()
    async def maps(self, inter, mode: Maps):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.mozambiquehe.re/maprotation?version=5&auth={apex_key}") as resp:
                data = json.loads(await resp.text())

                arenaEmbed = disnake.Embed(
                    title = "Arenas",
                    description = f"The current map for Arenas is {data['arenas']['current']['map']}."
                ).set_image(
                    url = data['arenas']['current']['asset']
                )

                
                rankedArenaEmbed = disnake.Embed(
                    title = "Ranked Arenas",
                    description = f"The current map for Ranked Arenas is {data['arenasRanked']['current']['map']}."
                ).set_image(
                    url = data['arenasRanked']['current']['asset']
                )

                
                battleRoyaleEmbed = disnake.Embed(
                    title = "Battle Royale",
                    description = f"The current map for Battle Royale is {data['battle_royale']['current']['map']}."
                ).set_image(
                    url = data['battle_royale']['current']['asset']
                )

                
                rankedBREmbed = disnake.Embed(
                    title = "Ranked Battle Royale",
                    description = f"The current map for Ranked Battle Royale is {data['ranked']['current']['map']}."
                ).set_image(
                    url = data['ranked']['current']['asset']
                )

                
                if mode == "arenas":
                    await inter.response.send_message(embed = arenaEmbed)
                elif mode == "arenasRanked":
                    await inter.response.send_message(embed = rankedArenaEmbed)
                elif mode == "battle_royale":
                    await inter.response.send_message(embed = battleRoyaleEmbed)
                elif mode == "ranked":
                    await inter.response.send_message(embed = rankedBREmbed)

    @apex.sub_command()
    async def crafting(self, inter):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.mozambiquehe.re/crafting?&auth={apex_key}") as resp:
                data = json.loads(await resp.text())
                craftingEmbed = disnake.Embed(
                    name = "Crafting Rotations",
                    description = f"""The next rotation is at <t:"""
                )
                
def setup(bot):
    bot.add_cog(Apex(bot))
    print("| Loaded the Apex Commands")