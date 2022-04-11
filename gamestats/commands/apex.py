import disnake
from disnake.ext import commands
import aiohttp
import os
from dotenv import load_dotenv
import json
from enum import Enum

load_dotenv()
apex_auth = os.environ["apex_auth"]

platforms = commands.option_enum({
    "PSN": "PS4",
    "PC": "PC",
    "XBOX": "X1"
})

maps = commands.option_enum({
    "Ranked Battle Royale": "ranked",
    "Ranked Arenas": "arenasRanked",
    "Battle Royale": "battle_royale",
    "Arenas": "arenas"
})

class Apex(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command()
    async def apex(self, inter):
        pass
    
    @apex.sub_command()
    async def maps(self, inter, mode: maps):
        async with aiohttp.ClientSession() as sesh:
            async with sesh.get(f"https://api.mozambiquehe.re/maprotation?version=5&auth={apex_auth}") as resp:
                data = json.loads(await resp.text())
                mapEmbed = disnake.Embed(
                    title = f"{maps(mode).name}!",
                    description = f"The current map for {maps(mode).name} is {data[mode]['current']['map'].title()}."
                ).set_image(
                    url = data[mode]['current']['asset']
                )
                    
        await inter.response.send_message(embed = mapEmbed)
        
    @apex.sub_command()
    async def predators(self, inter):
        async with aiohttp.ClientSession() as sesh:
            async with sesh.get(f"https://api.mozambiquehe.re/predator?version=5&auth={apex_auth}") as resp:
                data = json.loads(await resp.text())
                predEmbed = disnake.Embed(
                    title = "Predator Requirements!"
                    ).add_field(
                        name = "Battle Royale:",
                        value = 
                        f"PC: {data['RP']['PC']['val']} ; Total Masters + Preds: {data['RP']['PC']['totalMastersAndPreds']}\n"
                        f"PSN: {data['RP']['PS4']['val']} ; Total Masters + Preds: {data['RP']['PS4']['totalMastersAndPreds']}\n"
                        f"XBOX: {data['RP']['X1']['val']} ; Total Masters + Preds: {data['RP']['X1']['totalMastersAndPreds']}\n"
                        f"Switch: {data['RP']['SWITCH']['val']} ; Total Masters + Preds: {data['RP']['SWITCH']['totalMastersAndPreds']}"
                    ).add_field(
                        name = "Arenas:",
                        value = 
                        f"PC: {data['AP']['PC']['val']} ; Total Masters + Preds: {data['AP']['PC']['totalMastersAndPreds']}\n"
                        f"PSN: {data['AP']['PS4']['val']} ; Total Masters + Preds: {data['AP']['PS4']['totalMastersAndPreds']}\n"
                        f"XBOX: {data['AP']['X1']['val']} ; Total Masters + Preds: {data['AP']['X1']['totalMastersAndPreds']}\n"
                        f"Switch: {data['AP']['SWITCH']['val']} ; Total Masters + Preds: {data['AP']['SWITCH']['totalMastersAndPreds']}"
                        )
        await inter.response.send_message(embed = predEmbed)
    
    @apex.sub_command()
    async def stats(self, inter, user: str, platform: platforms):
        async with aiohttp.ClientSession() as sesh:
            async with sesh.get(f"https://api.mozambiquehe.re/bridge?version=5&platform={platform}&player={user}&auth={apex_auth}") as resp:
                data = json.loads(await resp.text())
                print(data)
                statsEmbed = disnake.Embed(
                    title = f"Stats for {data['global']['name']}"
                ).add_field(
                    name = "General Stats:",
                    value =
                        f"Name: {data['global']['name']}\n"
                        f"Last Platform: {data['global']['platform']}\n"
                        f"Banned: {data['global']['bans']['isActive']}\n"
                ).add_field(
                    name = "Ranks + RP/AP this split:",
                    value = f"Battle Royale: {data['global']['rank']['rankName']} {data['global']['rank']['rankDiv']}  - {data['global']['rank']['rankScore']} RP\n"
                    f"Arenas: {data['global']['arena']['rankName']} {data['global']['arena']['rankDiv']} - {data['global']['arena']['rankScore']} AP"
                    )
        await inter.response.send_message(embed = statsEmbed)

def setup(bot):
    bot.add_cog(Apex(bot))
    print("Apex Loaded.")