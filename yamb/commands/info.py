import disnake
from disnake.ext import commands

class Info(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def serverinfo(self, inter):
        guild = inter.guild
        infoEmbed = disnake.Embed(
            title = f"Server Info",
            description = 
                f"Name: {guild.name}\n"
                f"ID: {guild.id}\n"
                f"Owner: {guild.owner.mention} / {guild.owner}\n"
                f"Created At: {disnake.utils.format_dt(guild.created_at, 'D')}\n"
                f"Member Count (with bots): {guild.member_count}\n"
                f"Member Count (without bots): {guild.member_count - sum(member.bot for member in guild.members)}\n",
            colour = disnake.Colour.random()
        ).add_field(
            name = "Server Icon",
            value = f"[Icon URL]({guild.icon.url})"
        ).set_image(
            url = guild.icon.with_size(128).url
        )

        await inter.response.send_message(embed = infoEmbed)

def setup(bot):
    bot.add_cog(Info(bot))
    print("Loaded Info.")