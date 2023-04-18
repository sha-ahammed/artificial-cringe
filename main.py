from damo.vilab import proompt

import discord
import os  # default module
from dotenv import load_dotenv
from discord.file import File
from discord.commands import Option
from pair_zero import pair_zero

load_dotenv()  # load all the variables from the env file
bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")


@bot.slash_command(name="damo", description="use damo-vilab to generate gif")
async def proom(ctx, prompt: str):
    await ctx.defer()
    file_path = await proompt(prompt)
    with open(file_path, "rb") as generated_image:
        file = File(generated_image)
        await ctx.respond(f"Your prompt was {prompt}", file=file)
        os.remove(file_path)


@bot.slash_command(
    name="pair_zero", description="Use PAIR-Zero's Text2Video to generate gif"
)
async def video(
    ctx,
    prompt: Option(str, "proompt goes here", required=True),
    fps: Option(int, "FPS of gif", required=False, default=5),
    length: Option(int, "gif length, use integers", required=False, default=5),
):
    await ctx.defer()
    file_path = await pair_zero(prompt, fps, length)
    with open(file_path, "rb") as generated_image:
        file = File(generated_image)
        await ctx.respond(f"Your prompt was {prompt}", file=file)
        os.remove(file_path)


bot.run(os.getenv("TOKEN"))  # run the bot with the token
