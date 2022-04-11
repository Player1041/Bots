import disnake
from disnake.ext import commands


class Sticky(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    
    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        stickyEmbed = disnake.Embed(
            title = "Sticky Message",
            description = "J'adore pénis.")
        if message.channel.id == 951290492753154078 and message.author.id != self.bot.user.id:
            await message.channel.send(embed = stickyEmbed)
        async for messages in message.channel.history(limit=10):
            if message.embeds == IndexError:
                
def setup(bot):
    bot.add_cog(Sticky(bot))
    print("Loaded Stickies")