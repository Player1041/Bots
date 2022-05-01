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
                f":label: | Name: {guild.name}\n"
                f":id: | ID: {guild.id}\n"
                f":crown: | Owner: {guild.owner.mention} / {guild.owner}\n"
                f":date: | Created At: {disnake.utils.format_dt(guild.created_at, 'D')}\n"
                f":busts_in_silhouette: | Member Count (with bots): {guild.member_count}\n"
                f":bust_in_silhouette: | Member Count (without bots): {guild.member_count - sum(member.bot for member in guild.members)}\n",
            colour = disnake.Colour.random()
        ).add_field(
            name = "Server Icon",
            value = f"[Icon URL]({guild.icon.url})"
        ).set_image(
            url = guild.icon.with_size(128).url
        )
        await inter.response.send_message(embed = infoEmbed)


    @commands.slash_command()
    async def memberinfo(self, inter, member: disnake.User):
        """
        Displays the info of a given member.
        
        Parameters
        ----------
        member: The user who's info you want. Takes a member (@Yet Another Mod Bot#0829) or ID (963577351994736720)
        """
        
        userEmbed = disnake.Embed(
            title = "User Info",
            description = 
            f"Name: {member.name}\n"
            f"ID: {member.id}\n"
            f"User Creation Date:  {disnake.utils.format_dt(member.created_at, 'D')}"
            ).add_field(
                name = "User Avatar",
                value = f"[Avatar URL]({member.avatar.url})"
            ).set_image(
                url = member.avatar.with_size(128).url
            )
        if type(member) == disnake.User:
            await inter.response.send_message(embed = userEmbed)
        else:
            if member.premium_since is not None:
                boost = disnake.utils.format_dt(member.premium_since, 'D')
            else:
                boost = "Not a Booster"
            userEmbed.insert_field_at(
                index = 0,
                name = "Guild Member Info",
                value = 
                f"Nickname: {member.display_name}\n"
                f"Top Role: {member.top_role.mention}\n"
                f"Joined At: {disnake.utils.format_dt(member.joined_at, 'D')}\n"
                f"Boosted Since: {boost}"
                )
            await inter.response.send_message(embed = userEmbed)


def setup(bot):
    bot.add_cog(Info(bot))
    print("Loaded Info.")