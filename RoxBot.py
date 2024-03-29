import discord
from discord import app_commands
import random
import youtube_dl
import asyncio
import pafy
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

id_do_servidor = 0000000000000000 #Coloque aqui o ID do seu servidor

spotify_client_id = 'SPOTIFY_CI'
spotify_client_secret = 'SPOTIFY_CS'


class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False #Nós usamos isso para o bot não sincronizar os comandos mais de uma vez

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #Checar se os comandos slash foram sincronizados 
            await tree.sync(guild = discord.Object(id=id_do_servidor)) # Você também pode deixar o id do servidor em branco para aplicar em todos servidores, mas isso fará com que demore de 1~24 horas para funcionar.
            self.synced = True
        await self.change_presence(activity=discord.Game(name="Leitinho no Victor"))
        print(f"Entramos como {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'nescau', description='Nescau') #Comando específico para seu servidor
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Victor pegou no meu p@u!", ephemeral = False) 
    
@tree.command(guild = discord.Object(id=id_do_servidor), name = 'instagram', description='Siga Daanrox no Instagram') #Comando específico para seu servidor
async def slash3(interaction: discord.Interaction):
    await interaction.response.send_message(f"http://instagram.com/daanrox", ephemeral = False) 

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'jeba', description='Veja qual o tamanho da sua Jeba') #Comando específico para seu servidor
async def slash4(interaction: discord.Interaction):
    numero = random.randint(1,38)
    await interaction.response.send_message(f"Sua Jeba tem {numero} Cm", ephemeral = False) 
    

spotify_client_credentials_manager = SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret)
spotify_sp = spotipy.Spotify(client_credentials_manager=spotify_client_credentials_manager)



@tree.command(guild=discord.Object(id=id_do_servidor), name='play', description='Tocar música no canal de voz')
async def play_command(interaction: discord.Interaction):
    member = interaction.guild.get_member(interaction.user.id)
    if member.voice is None or member.voice.channel is None:
        await interaction.response.send_message('Você precisa estar em um canal de voz para usar este comando.', ephemeral=True)
        return

    channel = member.voice.channel
    if channel:
        voice_client = await channel.connect()

        mp3_path = 'music.mp3.mp3'

        if mp3_path:
            await interaction.response.send_message("Iniciando a música...")
            while True:
                voice_client.play(discord.FFmpegPCMAudio(mp3_path))
                while voice_client.is_playing():
                    await asyncio.sleep(1)

        await interaction.response.send_message("Vídeo reproduzido com sucesso!")
    else:
        await interaction.response.send_message("Você precisa estar em um canal de voz para usar este comando.")








aclient.run('TOKEN')