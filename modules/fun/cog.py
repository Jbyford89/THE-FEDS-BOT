import random
from nextcord.ext import commands
import asyncio

class Fun(commands.Cog, name="Fun"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    # Magic 8-ball
    @commands.command(aliases=["8ball", "8b"])
    async def _8ball(self, ctx: commands.Context, *, question: str):

        """Ask the magic 8-ball a question.
        
        Example: >_8ball Will I win the lottery?
        """

        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
        await ctx.send(f"🎱 {ctx.author.mention} asked: {question}\n🎱 {random.choice(responses)}")

        @commands.command()
        async def guess(ctx):
            await ctx.send('Guess a number between 1 and 10.')

            def is_correct(m):
                return m.author == ctx.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.bot.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await ctx.send('Sorry, you took too long it was {answer}.')

            if int(guess.content) == answer:
                await ctx.send('You are correct!')
            else:
                await ctx.send(f'Oops, it was {answer}.')

def setup(bot):
    bot.add_cog(Fun(bot))

