import discord

intents = discord.Intents.all()

client = discord.Client(intents=intents)


messages = {}


@client.event
async def on_ready():
    # Récupération du canal
    channel = client.get_channel(984956000845041695)
    async for message in channel.history(limit=50):
        if message.content == '':
            pass
        else:
            if message.author.name in messages.keys():
                if message.content not in messages[message.author.name]:
                    messages[message.author.name].append(message.content)
            else:
                messages[message.author.name] = []
                messages[message.author.name].append(message.content)

client.run("MTA2NzIyNDcxNTUxNDYxMzc5MQ.GWnrJj.09ibC13t-rPNP10ay2l0pqYlk2qqkHrvYvK4Eg")
