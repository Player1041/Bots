import disnake
from disnake.ext import commands

class Apps(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(Apps(bot))
    print("Loaded Applications!")