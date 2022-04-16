from nextcord.ext import commands
import time

class Ping(commands.Cog, name="Ping"):
    """Receives ping commands."""

    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Pong!
        
        For example, >ping returns ""🏓 WS: {before_ws}ms  |  REST: {int(ping)}ms""
        
        """

        before = time.monotonic()
        before_ws = int(round(self.bot.latency * 1000, 1))
        message = await ctx.send("🏓 Pong")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"🏓 WS: {before_ws}ms  |  REST: {int(ping)}ms")

def setup(bot):
    bot.add_cog(Ping(bot))