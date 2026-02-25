import random
import discord
from discord.ext import commands
from config import predict_image

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


ultimo_ejercicio_usuario = {}


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            archivo_name = archivo.filename
            archivo_url = archivo.url
            await archivo.save(f"./images/{archivo.filename}")
            await ctx.send(predict_image(f"./images/{archivo.filename}"))
    else:
        await ctx.send("no se a adjuntado ningun archivo.") 

