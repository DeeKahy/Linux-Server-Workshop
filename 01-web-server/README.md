# 01 - Host a Webpage

You're going to serve a real webpage from this server so anyone on the same network can visit it in their browser.

## How it works

- `server.py` starts a web server on **port 8080**
- It automatically serves `index.html` to anyone who visits
- No extra software needed - Python has this built in

## Steps

**1. Go into this folder**
```bash
cd 01-web-server
```

**2. Start the server**
```bash
python3 server.py
```

You should see:
```
Serving on http://0.0.0.0:8080
```

**3. Visit your page**

Open a browser and go to:
```
http://YOUR_SERVER_IP:8080
```

(Your server IP is on the piece of paper you were given.)

**4. Edit the page**

Open a new terminal (or press `ctrl+c` to stop the server first), then edit `index.html`:

```bash
nano index.html
```

Change some text, save with `ctrl+o` then `ctrl+x`, restart the server, and refresh your browser.

## Stop the server

```bash
ctrl + c
```

---

## Challenge ideas

- Change the heading and text in `index.html`
- Change the background colour (look for `background: #f0f4ff`)
- Add a second paragraph or a list of links
- Try serving on a different port by changing `PORT = 8080` in `server.py`
