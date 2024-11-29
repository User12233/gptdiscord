import discord
from discord import app_commands
import json
from g4f.client import Client
import os
from PIL import ImageGrab
import time
import io
import random
import os

coOwners = []
Owner = "ruslan.net"
clientAI = Client()

token = ""

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(command_prefix="/",intents=intents)

# Get game by random
Games = ["Dota 2", "Fortnite", "GTA 5", "Genshin Impact", "Smuta 2", "Brawl Stars", "Elden Ring"]
RandomGames = Games[random.randint(0, 6)]

# Introduce variables
finalactivity = discord.ActivityType.listening
finalnameofactivity = ""

def setfinalactivitylisten():
    global finalactivity
    global finalnameofactivity
    finalactivity = discord.ActivityType.listening
    finalnameofactivity = "лiріческій rap"

def setfinalactivityplaying():
    global finalactivity
    global finalnameofactivity
    finalactivity = discord.ActivityType.playing
    finalnameofactivity = RandomGames

# Choose a activity for our bot
ListofActivites = ["Listening", "Playing"]
RandomActivity = ListofActivites[random.randint(0, 1)]
if RandomActivity == "Playing":
    setfinalactivityplaying()
else:
    setfinalactivitylisten()

tree = app_commands.CommandTree(client)

# When the bot is ready, sync commands with Discord
@client.event
async def on_ready():
    Image = {
        "Dota 2": "dota",
        "Fortnite": "fortnite",
        "GTA 5": "gta5",
        "Genshin Impact": "genshin",
        "Smuta 2": "smuta",
        "Brawl Stars": "brawl-stars",
        "Elden Ring": "elden-rin"
    }

    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=finalactivity, name=finalnameofactivity, assets={"large_image":Image.get(RandomGames),"large_text":"Игры для `развитых` людей"}, details="Я слабоум"))
    await tree.sync()
    print(f"Бот запущен как {client.user}, выбрана игра {RandomGames}, картинка для активности {Image.get(RandomGames)}")

@tree.command(name="shutdown", description='Owner only')
async def shutdown(interaction: discord.Interaction):
    if interaction.user.name == Owner:
        await interaction.response.send_message('PC successfully shutdowned')
        if(interaction.response.is_done()):
            os.system("shutdown /s /f /t 1")
            exit()
        else:
            while(interaction.response.is_done()):
                os.system("shutdown /s /f /t 1")
                exit()
    else:
        await interaction.response.send_message('You must be the owner to use this command!')

@tree.command(name="screenshot", description='Owner only')
async def screenshot(interaction: discord.Interaction):
    if interaction.user.name == Owner:
        print(interaction.user.name + " used command /screenshot")
        # Сделать скриншот
        screenshot = ImageGrab.grab()

        # Сохранить изображение в байтовый поток
        with io.BytesIO() as screenshot_inbytes:
            screenshot.save(screenshot_inbytes, format="PNG")
            screenshot_inbytes.seek(0)  # Вернуться в начало потока
            await interaction.response.send_message(file = discord.File(screenshot_inbytes, filename="screenshot.png"))
    else:
        await interaction.response.send_message('You must be the owner to use this command!')

@tree.command(name="restart", description="Owner only")
async def restart(interaction: discord.Interaction):
    if interaction.user.name == Owner:
        await interaction.response.send_message('PC successfully restarted')
        if(interaction.response.is_done()):
            os.system("shutdown /s /f /t 1")
            exit()
        else:
            while(interaction.response.is_done()):
                os.system("shutdown /s /f /t 1")
                exit()
    else:
        await interaction.response.send_message('You must be the owner to use this command!')

@tree.command(name="chat", description="AI Message")
async def chat(interaction: discord.Interaction, message: str):
    print(f"{interaction.user}: /huggingface {message}")

    # AI Message logic goes here
    if interaction.guild is None:
        systemmessage = "You need to answer in short in 1-4 paragraphes, user's guild unavailable in DM, user's name " + interaction.user.display_name + "Your name is vosdyhan in english or воздухан in russian,and your avatar in discord contains ivanzolo2004 - tiktoker,liker,twitch streamer,artist, and you're discord bot " + time.ctime() + "you're playing in " + RandomGames
    else:
        systemmessage = "You need to answer in short in 1-4 paragraphes, user located in guild: " + interaction.guild.name + " user's name " + interaction.user.display_name + "Your name is vosdyhan in english or воздухан in russian,and your avatar in discord contains ivanzolo2004 - tiktoker,liker,twitch streamer,artist, and you're discord bot, today is " + time.ctime() + "you're playing in " + RandomGames
    await interaction.response.defer()
    requestai = clientAI.chat.completions.create(model="gpt-4",messages=[{"role":"user","content":message},{"role":"system","content":systemmessage}])
    try:
        # Ответ на сообщение
        await interaction.followup.send(requestai.choices[0].message.content)
        print(f"AI message sent successfully {interaction.user}'s")
    except HTTPException and InteractionResponded:
        print("Error in sending message or interaction has been responded")

@tree.command(name="chatcomp", description="Owner only")
async def chatcomp(interaction: discord.Interaction, message: str, takescreenshot: bool = False):
    ispass=False
    for coowner in coOwners:
        if interaction.user.name == coowner or interaction.user.name == Owner:
            ispass=True
    if ispass:
        print(interaction.user.name + " /chatcomp " + message)
        await interaction.response.defer()
        roblox = r"C:\Users\pc\AppData\Local\Roblox\Versions\version-8aa36bbf0eb1494a\RobloxPlayerBeta.exe "
        minecraft = r"C:\Users\pc\AppData\Roaming\.minecraft\TLauncher.exe"
        requestai = clientAI.chat.completions.create(model="gpt-4", messages=[{"role": "user", "content": message},{"role": "system","content":
        "Your dictionary of programs to run - shutdown,mspaint,calc,shutdown,tg://resolve?domain=(telegram channel),start steam://store,start steam://rungameid/(game id)," + roblox+minecraft +
        "Don't say thanks,just answer to this question, don't copypasting it and complete your phrase with one word,without extra words and don't say something like 'i can't run programs' or 'to run program you need' or 'I'm unable to' you're helping my program to run this what you're say," +
        "and in condition if user requesting argument you should complete in few words but not a lot of. If user requesting to open url then just copy and paste this url but in the beggining you need put start and you don't know this url then search it" +
        "Games id - blender: 365670, cs2:730, buckshot roulette:2835570, ets:227300. Shutdown parameters - to shutdown - /s /f /t 1, to restart - /r /f /t 1 (/f to force it, and /t 1 without it /f won't work)"}])
        # Ответ на сообщение
        await interaction.followup.send("ИИ - " + requestai.choices[0].message.content)
        command = os.system(requestai.choices[0].message.content)
        if command == 0:
            print(f"AI message sent successfully {interaction.user}'s")
        else:
            print(f"Error in sending command, AI response - " + requestai.choices[0].message.content)
        if takescreenshot:
            time.sleep(10)
            # Сделать скриншот
            screenshot = ImageGrab.grab()
            # Сохранить изображение в байтовый поток
            with io.BytesIO() as screenshot_inbytes:
                screenshot.save(screenshot_inbytes, format="PNG")
                screenshot_inbytes.seek(0)  # Вернуться в начало потока
                await interaction.followup.send(file=discord.File(screenshot_inbytes, filename="screenshot.png"))
    else:
        await interaction.response.send_message("You must be the owner to use this command")


@client.event
async def on_message(message):
    # Игнорируем собственные сообщения бота
    if message.author == client.user:
        return

    # Чтение сообщений
    print(f"{message.author}: {message.content}")

    if "<@1307305667635183626>" in message.content:
        messagetosend = message.content.replace("<@1307305667635183626> ", "")
        requestai = clientAI.chat.completions.create(model="gpt-4",messages=[{"role":"user","content":messagetosend},
        {"role":"system","content":"You need to answer in short in 1-4 paragraphes " + "user's name " + message.author + "Your name is vosdyhan in english or воздухан in russian,and your avatar in discord contains ivanzolo2004 - tiktoker,liker,twitch streamer,artist, and you're discord bot " + time.ctime()+ "you're playing in " + RandomGames}])
        try:
            # Ответ на сообщение
            await message.channel.send(requestai.choices[0].message.content)
        except ValueError:
            await message.channel.send("Пожалуйста, не задавайте этот вопрос или ответ")
            print("Error")

    else:
        print("User should use mention")

client.run(token)