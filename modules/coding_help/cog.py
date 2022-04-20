import datetime
import nextcord
from nextcord.ext import commands
from nextcord.utils import get

class CodingHelp(commands.Cog, name="Coding Help"):


    @commands.command(aliases=['ch', 'c-help'])
    async def coding_help(self, ctx: commands.Context, text: str):

        """Pings the Python Help role to get help on coding
        
        Example: `>coding_help python or >ch python`
        """

        # Ping the Python Help role
        ph = get(ctx.guild.roles, name='Python Help')
        if text.lower() == 'python':
            await ctx.send(f"{ph.mention}")
            e = nextcord.Embed(
                description=f"**python** help was requested by\n {ctx.author.mention}",
                colour=nextcord.Colour.blue(),
                type='rich',
                timestamp=datetime.datetime.now()
            )
            await ctx.message.channel.send(embed=e)
        else:
            await ctx.send(f"{ctx.author.mention} you have entered an invalid command.")

def setup(bot: commands.Bot):
    bot.add_cog(CodingHelp(bot))