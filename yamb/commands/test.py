import disnake
from disnake.ext import commands

class Test(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot



        
def setup(bot):
    bot.add_cog(Test(bot))
    print("Testing!")