import discord
from discord.ext  import commands


class Events:

	def __init__(self, bot):
		self.bot = bot


	async def on_command_error(self,ctx,error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("Input the correct arguments for this command")\

		if isinstance(error, commands.CommandNotFound):
			await ctx.send("Command Not Found")

		raise error