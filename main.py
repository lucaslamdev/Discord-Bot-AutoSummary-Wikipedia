import discord
import moedasapi
import wikipedia
import qrcodes
import asyncio
import os
import random
from discord.ext import commands
from replit import db
from keep_alive import keep_alive

cliente = commands.Bot(command_prefix='<>', case_insensitive=True)


@cliente.event
async def on_ready():
    print('Entramos como {0.user}' .format(cliente))
    await cliente.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="<>comandos"))


@cliente.command()
async def comandos(ctx):
    await ctx.send(" <>ola - Dá um olá para você.\n <>resumo assunto - Dá um resumo sobre o assunto pedido.\n <>aleatorio numero - Digite um valor máximo do sorteio e ele irá sortear algum numero entre 1 e o digitado. \n <>ping - Dá o ping entre você e o bot. \n <>dolar - Dá valor do dolar. \n <>euro - Dá valor do euro. \n <>qr - Gera um QR")


@cliente.command()
async def ping(ctx):
    await ctx.send(f"Ping de {cliente.latency:.3f}ms.")


@cliente.command()
async def dolar(ctx):
    valordolar = moedasapi.dolar()
    await ctx.send(f'Preço do dolar: R${valordolar:.2f}')


@cliente.command()
async def euro(ctx):
    valordolar = moedasapi.euro()
    await ctx.send(f'Preço do euro: R${valordolar:.2f}')


@cliente.command()
async def ola(ctx):
    await ctx.send(f'Olá, {ctx.author}')


@cliente.command()
async def resumo(ctx, *, topic):
    text = wikipedia.pesquisar(topic, ctx.author)
    titulo = text["title"]
    authortitulo = str(ctx.author)+str(titulo)
    arquivo = discord.File(authortitulo+"Resuminho.txt")
    await ctx.send(f"Titulo: {titulo}")
    await ctx.send(file=arquivo)
    await asyncio.sleep(2)
    os.remove(authortitulo+"Resuminho.txt")


@cliente.command()
async def qr(ctx, *, text):
    author = str(ctx.author)
    qrcodes.criar(text, author)
    arquivo = discord.File(author+"Resuminho.png")
    await ctx.send(file=arquivo)
    await asyncio.sleep(2)
    os.remove(author+"Resuminho.png")


@cliente.command()
async def aleatorio(ctx, numero):
    numero = int(numero)
    numaleatorio = random.randint(1, numero)
    await ctx.send(f'Numerozinho aleatorio escolhido é {numaleatorio}')

keep_alive()
cliente.run('DISCORD-BOT-KEY')
