import disnake
from disnake.ext import commands
import random

class Gay(commands.Cog):
	"""How gay are you?"""
	
	def __init__(self, bot: commands.Bot):
		self.bot = bot
		
	@commands.slash_command()
	async def gaydar(self, inter, user: disnake.Member):
		"""How gay are you?
		
		Parameters
		----------
		user: User rated for gayness.
		"""
		gay_level = random.randint(0,100)
		if user.id == 715943793500749925: #Dusty
			gay_level = 100
		if user.id == 459203015052623882: # Husko
			determiner = random.randint(0,10)
			if determiner == 6 or determiner == 9:
				gay_level = 69
			if determiner == 4 or determiner == 2:
				gay_level = 420
		gayEmbed = disnake.Embed(
			title = "Gaydar 3000",
			description = f"Hmm...\n{user.mention} is {gay_level}% gay!"
			).set_footer(
				text = "Player1041 is the Gaydar 🌈",
				icon_url = "https://media.discordapp.net/attachments/948022693096194098/948022718547263509/pfp.jpg"
				)
		await inter.response.send_message(embed=gayEmbed)
		
def setup(bot):
	bot.add_cog(Gay(bot))
	print("| Loaded The Gaydar 3000")
