import disnake
from disnake.ext import commands

class help(commands.Cog):
    """The help command."""
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.slash_command()
    async def help(self, inter):
        modEmbed = disnake.Embed(
            title = "Moderation!",
            description = """`/purge`
            \nPurges x amount of messages based on the `messages:` option.""")
        funEmbed = disnake.Embed(
            title = "Fun!",
            description = """`/colours`
            \nShows the info of a colour based on the hex code.""")
        disarrayEmbed = disnake.Embed(
            title = "Bot Info!",
            description = """`/disarray info`
            \nDisplays the info about the bot.
            \n`/disarray credits`
            \nDisplays the bots credits.""")
            
        embeds = [modEmbed, funEmbed, disarrayEmbed]
        
def setup(bot):
    bot.add_cog(help(bot))
    print("| Loaded the helper")