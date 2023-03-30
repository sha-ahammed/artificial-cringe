from damo.vilab import proompt

import discord
import os  # default module
from dotenv import load_dotenv
from discord.file import File

load_dotenv()  # load all the variables from the env file
bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")


@bot.slash_command(name="proompt", description="Send your proompts here proomptcel")
async def proom(ctx, prompt: str):
    await ctx.defer()
    file_path = await proompt(prompt)
    with open(file_path, "rb") as generated_image:
        file = File(generated_image)
        await ctx.respond(f"Your prompt was {prompt}", file=file)
        os.remove(file_path)


bot.run(os.getenv("TOKEN"))  # run the bot with the token
