import disnake
from disnake.ext import commands


class disarray(commands.Cog):
    """A command set to do with Disarray's Info"""
    
    def __init__(self, bot: commands.Cog):
        self.bot = bot
        
    @commands.slash_command()
    async def disarray(self, inter):
        pass
    
    @disarray.sub_command()
    async def credits(self, inter):
        """Roll the credits!"""
        creditsEmbed = disnake.Embed(
            title = "Disarray - A Project by Player1041",
            description = "Disarray is a personal project created by Player1041.",
            colour = disnake.Colour.random()
            ).add_field(
                name = "Libraries",
                value = f"""Main Bot Library: [Disnake](https://github.com/DisnakeDev/disnake)"""
            ).add_field(
                name = "Helpful People",
                value = """The following were very helpful during the development of Disarray:
                \nSmU#4818 - Command Tester
                \nA lot of people in the [Disnake Server](https://discord.gg/disnake)
                \nA lot of people in the [Python Discord Server](https://discord.gg/python)"""
            ).set_footer(
                text = "Made by Player1041 with <3",
                icon_url = "https://media.discordapp.net/attachments/951479012302155836/951966892791332954/Picsart_22-03-11_10-02-24-899992.png?width=540&height=540"
            )
                
        await inter.response.send_message(embed = creditsEmbed)
        
    @disarray.sub_command()
    async def info(self, inter):
        deez = inter.me
        joined = deez.joined_at.timestamp()
        owner = await self.bot.fetch_user(self.bot.owner_id)
        infoEmbed = disnake.Embed(
            title = "Info!",
            colour = disnake.Colour.random()
        ).add_field(
            name = "Name:",
            value = f"{deez.name} ({deez.mention})"
        ).add_field(
            name = "ID",
            value = deez.id
        ).add_field(
            name = "Developer",
            value = f"{owner.name} ({owner.mention})"
        ).add_field(
            name = "Servers",
            value = f"""Guilds: {len(self.bot.guilds)}
            \nMembers: {len(self.bot.users)}
            """
        )
        delButton = disnake.ui.Button(
            emoji = "🗑️",
            style = disnake.ButtonStyle.red,
            custom_id = "delete",)
        await inter.response.send_message(embed = infoEmbed, components = delButton)

    @commands.Cog.listener("on_button_click")
    async def del_button(self, inter):
        if inter.component.custom_id != "delete":
            return
        if inter.user != self.author:
            return
        await inter.message.delete()
def setup(bot):
    bot.add_cog(disarray(bot))
    print("| Loaded all Disarray Commands.")