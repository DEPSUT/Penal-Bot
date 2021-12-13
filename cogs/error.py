from discord.ext import commands


class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Shows when the cog has been loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has loaded.")


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            print(f"{str(error)}")


def setup(bot):
    bot.add_cog(Error(bot))