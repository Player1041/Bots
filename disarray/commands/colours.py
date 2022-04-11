import disnake
from disnake.ext import commands
from PIL import Image
import os

class colours(commands.Cog):
    """A set of colour commands."""
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command()
    async def colours(self, inter):
        pass
    
    @colours.sub_command()
    async def rgb(self, inter, red: commands.Range[0,255], green: commands.Range[0,255], blue: commands.Range[0,255]):
        img = Image.new('RGB', (50, 50), (red, green, blue))
        img.save('commands/assets/colour_rgb.png')
        hex = f"{red*255}"
        colourEmbed = disnake.Embed(
            title = "Colours!",
            description = "This is your colour!"
        ).add_field(
            name = "Hex:",
            value = "hex"
        ).set_image(
            file = disnake.File(
                'commands/assets/colour_rgb.png'
            )
        )
        await inter.response.send_message(embed = colourEmbed)
        os.remove('commands/assets/colour_rgb.png')

def setup(bot):
    bot.add_cog(colours(bot))
    print("| Loaded All Colour Commands")