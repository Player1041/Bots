import disnake
from disnake.ext import commands
import os
class commands(commands.Cog):
    """A set of cogs management commands."""
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.slash_command()
    @commands.is_owner()
    async def command(self, inter):
        pass
    
    @command.sub_command(guild_ids = 951289542684590140)
    @commands.is_owner()
    async def reload(self, inter, catagory: str):
        """Reloads a specific set of commands.
        
        Parameters
        ----------
        catagory - The command you will reload.
        """
        channel = self.bot.get_channel(952376845368692798)
        self.bot.reload_extension(f"commands.{catagory}")
        
        await channel.send(embed = disnake.Embed(
            title = "Reload!",
            description = f"Reloaded the {catagory.title()} commands by {inter.author.mention}",
            colour = disnake.Colour.random()))
        
        await inter.response.send_message("Check <#952376845368692798>")
    
    @reload.autocomplete("catagory")
    async def catagory_autocomp(self, inter, str): 
        return [ext.split(".")[-1] for ext in self.bot.extensions]
    
    @reload.error
    async def reloadError(self, inter, exception):
        actual = exception.original if isinstance(exception, commands.CommandInvokeError) else exception
        missingErrorEmbed = disnake.Embed(
    	title = "Error!",
		description = "That cog was not loaded. It either didn't load correctly or does not exist.")

        if isinstance(actual, disnake.Forbidden):
            await inter.response.send_message(embed = permsErrorEmbed)
            return
        raise
def setup(bot):
    bot.add_cog(commands(bot))
    print("| Loaded all Command Management Commands")