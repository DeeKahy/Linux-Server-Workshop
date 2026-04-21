# 04 - Flask REST API

Most of the web runs on APIs - your phone apps, websites, and services all talk to servers by sending HTTP requests and getting back JSON. Here you'll build one yourself.

This API lets you post messages and read them back. Nothing fancy, but the same pattern is used in production apps everywhere.

---

## Steps

**1. Go into this folder**
```bash
cd 04-flask-api
```

**2. Install Flask**
```bash
pip3 install -r requirements.txt
```

**3. Start the API**
```bash
python3 app.py
```

You should see:
```
API running on http://0.0.0.0:5000
```

---

## Try it out

Open a **second terminal** (keep the API running in the first one) and use `curl` to talk to it.

**Check it's alive:**
```bash
curl http://localhost:5000/ping
```
```json
{"response": "pong"}
```

**Post a message:**
```bash
curl -X POST http://localhost:5000/messages \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello from the terminal!"}'
```

**Read all messages:**
```bash
curl http://localhost:5000/messages
```

You can also open `http://YOUR_SERVER_IP:5000` in a browser.

---

## What is JSON?

JSON is just a way of formatting data so programs can read it easily. It looks like this:

```json
{"name": "Alice", "age": 25, "likes": ["coding", "coffee"]}
```

---

## Challenge ideas

- Add a `/messages/<id>` route that returns a single message by its ID
- Add a `name` field to each message so you can sign your posts
- Add a `DELETE /messages` route that clears all messages
- Connect this API to the web server from project 01 - fetch and display messages in the browser using JavaScript
