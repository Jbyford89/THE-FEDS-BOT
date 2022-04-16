import random
from nextcord.ext import commands


class Random(commands.Cog, name="Random"):
    """Returns random results."""

    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx: commands.Context, dice: str):
        """Rolls a dice in NdN format.
        
        For example, >roll 2d6 returns one six-sided die and one six-sided die.
        """
        try:
            rolls = ""
            amount, die = dice.split("d")
            for _ in range(int(amount)):
                roll = random.randint(1, int(die))
                rolls += f"{roll}, "
            await ctx.send(f"🎲 {ctx.author.mention} rolled {dice}: {rolls[:-2]}")
        except ValueError:
            await ctx.send("Format has to be in NdN! (example: '2d6')")

    @commands.command()
    async def choose(self, ctx: commands.Context, *choices: str):
        """Chooses between multiple options.
        
        Example: `>choose option1 option2 option3`
        """
        choice = random.choice(choices)
        await ctx.send(f"🤔 {ctx.author.mention} chose: {choice}")

    @commands.command()
    async def flip(self, ctx: commands.Context):
        """Flips a coin.
        
        An example: >flip
        Results in format: 🎲 {ctx.author.mention} flipped a coin and got {result}
        """
        choice = random.choice(["heads", "tails"])
        await ctx.send(f"👛 {ctx.author.mention} flipped a coin: {choice}")


def setup(bot):
    bot.add_cog(Random(bot))
