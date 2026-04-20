# 02 — Discord Ping/Pong Bot

You're going to run a Discord bot on this server. When someone types `!ping` in Discord, the bot replies `Pong!`.

## Before you start

You need a **bot token**. This is like a password that lets your code log in as the bot.

### Get a token (if you don't have one)

1. Go to https://discord.com/developers/applications
2. Click **New Application**, give it a name
3. Go to the **Bot** tab on the left
4. Click **Reset Token** and copy it — you only see it once!
5. Scroll down and turn on **Message Content Intent**
6. Go to **OAuth2 → URL Generator**, tick `bot`, tick `Send Messages` and `Read Messages`
7. Copy the generated URL and open it to invite the bot to a server you own

---

## Steps

**1. Go into this folder**
```bash
cd 02-discord-bot
```

**2. Install the discord.py library**
```bash
pip3 install -r requirements.txt
```

**3. Add your token**

Open `bot.py`:
```bash
nano bot.py
```

Find this line:
```python
TOKEN = "PASTE_YOUR_TOKEN_HERE"
```

Replace `PASTE_YOUR_TOKEN_HERE` with your actual token. Save with `ctrl+o` then `ctrl+x`.

**4. Run the bot**
```bash
python3 bot.py
```

You should see:
```
Logged in as YourBot#1234
Bot is online!
```

**5. Test it**

Go to your Discord server and type `!ping` — the bot should reply `Pong! 🏓`

## Stop the bot

```bash
ctrl + c
```

---

## Challenge ideas

- Add a `!roll` command that replies with a random number from 1–6 (hint: `import random`)
- Add a `!time` command that replies with the current time (hint: `import datetime`)
- Make the bot reply differently depending on who sent the message
