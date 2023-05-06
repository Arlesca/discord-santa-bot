from random import randint
from os.path import exists
from os import getenv
import discord

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'I am logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if client.user.mentioned_in(message):
        if not exists("./SantaDone"):
            recivs = []
            givers = recivs.copy()

            await message.channel.send("Dags att ge ut presenter!\nAlla som deltar ska ha fått ett meddelande med namnet på personen du ska ge en present till!", file=discord.File("res/pepe-christmas.gif"))
            
            for member in message.channel.guild.members:    
                if member.nick in givers:
                    while True:
                        recivIndx = randint(0, (len(givers) - 1))
                        giftRecvr = recivs[recivIndx]

                        # Makes sure members don't give a gift to themself
                        if not giftRecvr in member.nick:
                            print(givers)
                            print(f"Delar ut till: {member.nick}")
                            await member.send(content="Dags för secret santa!\nDu ska köpa en present till {0}.".format(giftRecvr))
                            print(f"{member.nick} fick {giftRecvr}")
                            givers.remove(member.nick)
                            recivs.remove(giftRecvr)
                            break
                    
                    print("\n")
        else:
            await message.channel.send("Alla har redan fått sin mottagare utdelad.\nGå och skaffa en present!")

client.run(getenv("DISCORD_BOT_TOKEN"))