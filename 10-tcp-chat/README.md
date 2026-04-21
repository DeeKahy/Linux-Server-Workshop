# 07 - TCP Chat Server

This one is different from the others - it's a **multiplayer** project. One person in the room runs the server, and everyone else connects to it. You can all send messages to each other in real time, directly through the terminal.

No internet required. It works entirely over the local network.

---

## How it works (the simple version)

Your computer and the server are connected by a **socket** - basically a pipe between two programs. This project opens that pipe up to multiple people at once. When you type a message, it goes to the server, and the server forwards it to everyone else.

---

## There are two roles

| Role | Who does it | What they run |
|------|-------------|---------------|
| **Server** | One person (e.g. the workshop host) | `python3 server.py` |
| **Client** | Everyone else | `python3 client.py SERVER_IP` |

---

## Running the server

Only **one person** does this step.

```bash
cd 07-tcp-chat
python3 server.py
```

You'll see:
```
Chat server running on port 9999
Others can connect with:  python3 client.py YOUR_SERVER_IP
Waiting for connections...
```

The server terminal will show you who connects and disconnects, and print every message. **Don't close this terminal** - the chat dies if you do.

Tell everyone else your IP address so they can connect.

---

## Connecting as a client

Everyone else runs this (replace `10.0.0.5` with the server's actual IP):

```bash
cd 07-tcp-chat
python3 client.py 10.0.0.5
```

It will ask for your name, then you're in. Type a message and press Enter to send.

```
Server IP address: 10.0.0.5
Your name: Alice
Connected! Type a message and press Enter. Ctrl+C to quit.

>> Bob joined the chat
Bob: hey everyone
```

---

## Stopping

- **Clients:** press `ctrl+c`
- **Server:** press `ctrl+c` (this disconnects everyone)

---

## What's actually happening?

- `server.py` listens on **port 9999** for incoming connections
- Each time someone connects, it starts a new **thread** - a separate mini-program running in parallel - to handle that person
- When a message arrives from one client, `broadcast()` loops through all connected clients and sends it to each one
- `client.py` also uses a thread: one for receiving messages (so they appear automatically) and one for sending (reading your input)

---

## Challenge ideas

- Add a `/quit` command that disconnects you cleanly with a goodbye message
- Add a `/users` command that lists everyone currently in the chat
- Show the time next to each message (hint: `import datetime`)
- Make the server log all messages to a file so you can read the history later
- Try connecting more than 5 people - does it hold up?
