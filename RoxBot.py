import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='/', description="Meus comandos:", intents=intents)
token = "MTA1MDAzNDk1MDE2ODEzNzc4OA.G7L4m9._Z6fux0vAERGgYDiJ_5P70R9ZC1fD2bq0Pz4o0"
invite_url = "https://discord.com/api/oauth2/authorize?client_id=1050034950168137788&permissions=2147699777&scope=bot"

probabilidade_reacao = 0.2  # 20% de probabilidade de reagir


@bot.event
async def on_ready():
    print('Estou conectado ao Discord!')
    await bot.change_presence(activity=discord.Game(name="o pau na sua cara!"))
    await bot.user.edit(description=f"Experimente meus comandos com /jeba\nAdicione-me ao seu servidor: [{invite_url}]")

@bot.event
async def on_message(message):
    if 'opa' in message.content.lower():
        await message.add_reaction('❤️')
    await bot.process_commands(message)

@bot.event
async def on_message(message):
    if message.channel.id == 823995232743850082:
        if random.random() < probabilidade_reacao:
            await message.add_reaction('🍆')
    await bot.process_commands(message)

@bot.command()
async def jeba(ctx):
    tamanho = random.randint(7, 40)
    await ctx.send(f"{ctx.author.mention} tem {tamanho}cm de Jeba")



@bot.command()
async def nescau(ctx):
    await ctx.send(f"{ctx.author.mention} chupou meu pau!")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(823995232743850082)
    
    embed = discord.Embed(title="Olha essa maravilha que chegou no servidor! :heart_eyes:", color=0xFF5733)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Nome:", value=member.display_name, inline=False)
    embed.add_field(name="Entrou em:", value=member.joined_at.strftime("%d/%m/%Y às %H:%M:%S"), inline=False)

    await channel.send(embed=embed)

bot.run(token)
