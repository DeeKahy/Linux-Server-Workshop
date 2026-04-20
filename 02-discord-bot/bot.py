import discord

# Paste your bot token here (keep it secret!)
TOKEN = "PASTE_YOUR_TOKEN_HERE"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    print("Bot is online! Try sending !ping in a Discord channel.")

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    if message.content == "!ping":
        await message.channel.send("Pong! 🏓")

    if message.content == "!hello":
        await message.channel.send(f"Hey {message.author.name}! 👋")

client.run(TOKEN)
