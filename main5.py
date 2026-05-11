import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 6):
    await ctx.send("he" * count_heh)

@bot.command()
async def help(ctx):

    comandos = ""

    for comando in bot.commands:
        comandos += f"!{comando.name}\n"

    await ctx.send(f" Comandos do bot:\n```{comandos}```")

@bot.command()
async def Sigma(ctx):
    await ctx.send("Sigma, são os melhores de todos os tempos, são os mais fortes, os mais inteligentes, os mais bonitos, os mais ricos, os mais poderosos, os mais influentes, os mais respeitados, os mais admirados, os mais temidos, os mais amados, os mais odiados, os mais invejados, os mais desejados, os mais cobiçados, os mais almejados, os mais sonhados, os mais idolatrados, os mais venerados, os mais reverenciados, os mais adorados, os mais cultuados, os mais exaltados, os mais glorificados, os mais santificados, os mais divinizados🗿🗿🗿")

@bot.command()
async def adivinhar(ctx, chute: int):
    import random
    
    numero = random.randint(1, 10)

    if chute < 1 or chute > 10:
        await ctx.send("escolhe um número de 1 a 10!")
        return

    if chute == numero:
        await ctx.send(f"acertou! O número era {numero}")
    else:
        await ctx.send(f"errou! Era {numero}")

@bot.command()
async def troca_de_notas(ctx):
    await ctx.send("Quais são as notas que você quer trocar😁?.\nQuer saber,Não!, vai estudar, HAHAHAHAHAHAHAHAHA")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, membro:discord.member, motivo="Sem motivo"):
    await membro.kick(reason=motivo)
    await ctx.send(f" {membro} foi kickado!")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def limpar(ctx, quantidade: int = 1000):
    await ctx.channel.purge(limit=quantidade + 1)
    msg = await ctx.send(f'Limpeza feita! Limpei {quantidade} sujeirices.')
    await msg.delete(delay=3)

bot.run("token")
