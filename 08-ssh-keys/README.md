# 09 - SSH Keys

> **Warning:** I have NOT properly tested this on every operating system



Right now you're logging in with a password. That works, but passwords can be guessed, brute-forced, or accidentally leaked.

**SSH keys** are a more secure alternative. Instead of a password, you use a matched pair of files:

- **Private key** - stays on your computer, never shared with anyone
- **Public key** - goes on the server, like a lock that only your private key can open

When you connect, SSH does a quick cryptographic check. If your private key matches the public key on the server, you're in.

---

## Step 1 - Generate a key pair on YOUR computer

Do this on your **own laptop**, not on the server. Open a terminal (or PowerShell on Windows).

### Mac / Linux


```bash
ssh-keygen -t ed25519 -C "your-name"
```

Press Enter to accept the default file location. You can set a passphrase for extra security, or just press Enter to skip.

This creates two files:
- `~/.ssh/id_ed25519` - your **private key** (never share this)
- `~/.ssh/id_ed25519.pub` - your **public key** (this goes on the server)

### Windows - PowerShell (Windows 10 / 11)

`ssh-keygen` is built into modern Windows. Open PowerShell and run the exact same command:

```powershell
ssh-keygen -t ed25519 -C "your-name"
```

Your keys are saved in:
- `C:\Users\YourName\.ssh\id_ed25519`
- `C:\Users\YourName\.ssh\id_ed25519.pub`


---

## Step 2 - Copy your public key to the server

### Mac / Linux - easy way

```bash
ssh-copy-id ubuntu@YOUR_SERVER_IP
```

Enter your password once. It automatically adds your key to the right place on the server. Done.

### Mac / Linux / Windows PowerShell - manual way

First, print your public key:

```bash
# Mac / Linux
cat ~/.ssh/id_ed25519.pub

# Windows PowerShell
type $env:USERPROFILE\.ssh\id_ed25519.pub
```

Copy the whole line - it starts with `ssh-ed25519` and ends with your comment.

Now on the **server**, run:

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
nano ~/.ssh/authorized_keys
```

Paste your public key on a new line. Save with `ctrl+o` then `ctrl+x`.

Then set the correct permissions:

```bash
chmod 600 ~/.ssh/authorized_keys
```

> **Permissions matter.** SSH will silently refuse to use keys if the file permissions are too open. `600` means only your user can read it.

---

## Step 3 - Test it

Open a **new terminal** (keep your existing session open just in case) and connect:

```bash
ssh ubuntu@YOUR_SERVER_IP
```

If it logs you in without asking for a password, it worked.

---

## Why ed25519?

There are a few key types (RSA, ECDSA, ed25519). **ed25519** is the modern recommended choice - it's shorter, faster, and more secure than the older RSA format you might see elsewhere.

