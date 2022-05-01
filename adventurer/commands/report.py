import disnake
from disnake.ext import commands

class Report(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(Report(bot))
    print("Loaded Reporting!")