import discord
from discord.ext import commands, tasks
import random
from newsapi import NewsApiClient


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='/', description="Meus comandos: /jeba /noticias", intents=intents)
token = "MTA1MDAzNDk1MDE2ODEzNzc4OA.G7L4m9._Z6fux0vAERGgYDiJ_5P70R9ZC1fD2bq0Pz4o0"
invite_url = "https://discord.com/api/oauth2/authorize?client_id=1050034950168137788&permissions=2147699777&scope=bot"

newsapi = NewsApiClient(api_key='637cf9f4e9854899b0b2ac097e3085eb')

probabilidade_reacao = 0.2  # 20% de probabilidade de reagir
news_channel_id = 823995232743850082  # substitua pelo ID do canal onde as notícias serão publicadas

@bot.event
async def on_ready():
    print('Estou conectado ao Discord!')
    await bot.change_presence(activity=discord.Game(name="o pau na sua cara!"))
    await bot.user.edit(description=f"Experimente meus comandos com /jeba\nAdicione-me ao seu servidor: [{invite_url}]")
    news_updates.start()

@tasks.loop(hours=12)
async def news_updates():
    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(q='games, jogos, esports, gta, rocketleague, rocket league, rockstar games', category='entertainment', language='pt')

    # Seleciona 2 notícias aleatórias
    selected_articles = random.sample(top_headlines['articles'], k=2)

    # Publica as notícias selecionadas no canal
    channel = bot.get_channel(news_channel_id)
    for article in selected_articles:
        embed = discord.Embed(title=article['title'], url=article['url'], description=article['description'], color=discord.Color.blue())
        embed.set_image(url=article['urlToImage'])
        await channel.send(embed=embed)

@bot.command()
async def noticias(ctx):
    top_headlines = newsapi.get_top_headlines(q='games, jogos, esports, gta, rocketleague, rocket league, rockstar games', category='entertainment', language='pt')
    selected_article = random.choice(top_headlines['articles'])
    embed = discord.Embed(title=selected_article['title'], url=selected_article['url'], description=selected_article['description'], color=discord.Color.blue())
    embed.set_image(url=selected_article['urlToImage'])
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    if 'opa' in message.content.lower():
        await message.add_reaction('❤️')
    elif message.channel.id == 823995232743850082:
        if random.random() < probabilidade_reacao:
            await message.add_reaction('🍆')
    await bot.process_commands(message)

@bot.command()
async def jeba(ctx):
    tamanho = random.randint(7, 40)
    await ctx.send(f"{ctx.author.mention} tem {tamanho}cm de Jeba")

@bot.command()
async def nescau(ctx):
    await ctx.send(f"{ctx.author.mention} beijou meu pau!")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(823995232743850077)
    
    embed = discord.Embed(title="Olha essa maravilha que chegou no servidor! :heart_eyes:", color=0xFF5733)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Nome:", value=member.display_name, inline=False)
    embed.add_field(name="Entrou em:", value=member.joined_at.strftime("%d/%m/%Y às %H:%M:%S"), inline=False)

    await channel.send(embed=embed)

bot.run(token)