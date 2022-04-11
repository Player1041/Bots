import disnake
from disnake.ext import commands

class Purge(commands.Cog):
    """It's a purge command."""
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages = True)
    async def purge(self, inter, messages: int):
        channel = inter.channel
        
        deleted = await channel.purge(limit = messages, bulk = True)
        successEmbed = disnake.Embed(
            title = "Successful!",
            description = f"{inter.author.mention} has purged {len(deleted)} messages."
        )
        await inter.response.send_message(embed = successEmbed)
    
    @purge.error
    async def purge_error(self, inter, exception):
        invoked = exception.original if isinstance(exception, commands.CommandInvokeError) else exception
        missingPermsEmbed = disnake.Embed(
            title = "Error!",
            description = "You are missing the Manage Messages permission.")
           
        botMissingPermsEmbed = disnake.Embed(
            title = "Error!",
            description = "I am missing the Manage Messages permission.")

        if isinstance(exception, commands.MissingPermissions):
            await inter.response.send_message(embed = missingPermsEmbed)
            return
        elif isinstance(exception, commands.BotMissingPermissions):
            await inter.response.send_message(embed = botMissingPermsEmbed)
            return
        raise
def setup(bot):
    bot.add_cog(Purge(bot))
    print("| Loaded The Purge.")