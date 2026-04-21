# 08 - UFW Firewall

Your server is reachable over the network - which means anyone on the same network could try to connect to any port on it. A **firewall** lets you control exactly which ports are open and which are blocked.

**UFW** (Uncomplicated Firewall) is the standard firewall tool on Ubuntu. It wraps the more complex `iptables` into simple commands.

---

## What is a port?

Think of your server like a building. The IP address is the street address. **Ports are the doors** - each one leads to a different service.

| Port | Usually used for |
|------|-----------------|
| 22   | SSH (how you're connected right now) |
| 80   | HTTP websites |
| 443  | HTTPS websites |
| 8080 | Common alternative web port |
| 5000 | Flask apps |

By default, a fresh server has no firewall rules - every door is open.

---

## Step 1 - Check the current status

```bash
sudo ufw status verbose
```

If UFW is inactive, nothing is being blocked yet.

---

## Step 2 - Set the defaults

Before turning UFW on, set sensible defaults:

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

This means: **block everything coming in, allow everything going out** - unless you explicitly open a port.

---

## Step 3 - Allow SSH first (important!)

> **Warning:** If you enable the firewall without allowing SSH first, you will lock yourself out of the server and lose your connection.

```bash
sudo ufw allow ssh
```

This is the same as `sudo ufw allow 22` because ssh uses port 22 by default.

---

## Step 4 - Enable the firewall

```bash
sudo ufw enable
```

Check it's on:

```bash
sudo ufw status verbose
```

---

## Step 5 - Allow and block ports

Allow a port (e.g. the web server from project 01):
```bash
sudo ufw allow 8080
```

Allow only TCP traffic on a port:
```bash
sudo ufw allow 5000/tcp
```

Block a port:
```bash
sudo ufw deny 3306
```

---

## Step 6 - List and delete rules

List all rules with numbers:
```bash
sudo ufw status numbered
```

Delete a rule by its number:
```bash
sudo ufw delete 3 # make sure this is NOT port 22
```

Or delete by name:
```bash
sudo ufw delete allow 8080
```

---

## If you get locked out

Disable the firewall:
```bash
sudo ufw disable
```

Wipe all rules and start over:
```bash
sudo ufw reset
```

---

## Quick reference

| Command | What it does |
|---------|-------------|
| `sudo ufw status verbose` | Show all rules and current status |
| `sudo ufw enable` | Turn the firewall on |
| `sudo ufw disable` | Turn the firewall off |
| `sudo ufw allow 8080` | Open port 8080 |
| `sudo ufw deny 8080` | Block port 8080 |
| `sudo ufw delete allow 8080` | Remove a rule |
| `sudo ufw reset` | Wipe all rules |

---

## Challenge ideas

- Enable UFW, allow SSH and port 8080, then run the web server from project 01 and confirm you can still reach it in the browser
- Block port 8080 while the web server is running - what happens?
- Allow port 5000, run the Flask API from project 04, and confirm it responds
- Run `sudo ufw status numbered` after each change and watch the rule list grow
