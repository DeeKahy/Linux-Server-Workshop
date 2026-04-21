# Server Workshop

Welcome! In this workshop you'll be running real code on a real Linux server.

You're connected via SSH - that means you're typing commands directly on a machine that could be anywhere in the world. Pretty cool.

## Projects

| # | Project | What you'll learn |
|---|---------|-------------------|
| [01-web-server](./01-web-server/) | Host a webpage | Python, HTTP, ports |
| [02-discord-bot](./02-discord-bot/) | Discord ping/pong bot | Bots, tokens, APIs |
| [03-systemd-service](./03-systemd-service/) | Run a program as a service | systemd, background processes |
| [04-flask-api](./04-flask-api/) | Build a tiny REST API | Flask, JSON, routes |
| [05-bash-scripting](./05-bash-scripting/) | Write shell scripts | Variables, loops, conditionals |
| [06-cron-jobs](./06-cron-jobs/) | Schedule tasks | crontab, automation |
| [07-ufw-firewall](./07-ufw-firewall/) | Control open ports | UFW, firewall rules |
| [08-ssh-keys](./08-ssh-keys/) | Passwordless SSH login | Key pairs, authorized_keys |
| [09-auto-updates](./09-auto-updates/) | Keep the server patched | apt, unattended-upgrades |
| [10-tcp-chat](./10-tcp-chat/) | Multiplayer chat server | Sockets, threads, networking |

## Getting started

Clone this repo onto the server:

```bash
git clone https://github.com/YOUR_USERNAME/server-workshop.git
cd server-workshop
```

Then pick a project folder and read its `README.md`.

---

## Getting around

```bash
ls                  # list files in the current folder
ls -la              # list files including hidden ones, with permissions
cd foldername       # go into a folder
cd ..               # go back up one level
cd ~                # go to your home folder
pwd                 # print the current folder path
```

> **Tip:** If something goes wrong, `ctrl + c` almost always stops it safely.

---

## Linux command reference

### Files and folders

```bash
cat file.txt            # print a file's contents
nano file.txt           # open a file in the nano text editor
                        #   save: ctrl+o  |  exit: ctrl+x
cp file.txt copy.txt    # copy a file
mv file.txt other.txt   # move or rename a file
rm file.txt             # delete a file (no undo!)
mkdir foldername        # create a folder
rm -r foldername        # delete a folder and everything in it
find . -name "*.py"     # find files matching a pattern
```

### Running programs

```bash
python3 script.py       # run a Python script
chmod +x script.sh      # make a shell script executable
./script.sh             # run a shell script
which python3           # find where a program is installed
```

### Packages

```bash
sudo apt update             # refresh the list of available packages
sudo apt install <name>     # install a package
sudo apt remove <name>      # remove a package
pip3 install <name>         # install a Python package
```

### Processes

```bash
ps aux                  # list all running processes
top                     # live view of processes and CPU/memory usage
kill <pid>              # stop a process by its ID
ctrl + c                # stop the program running in the current terminal
ctrl + z                # pause the program (bg to resume in background)
```

### Network

```bash
ip a                    # show network interfaces and IP addresses
curl http://...         # make an HTTP request from the terminal
ss -tlnp                # show which ports are open and listening
```

### System

```bash
df -h                   # disk usage
free -h                 # memory usage
uptime                  # how long the server has been running
whoami                  # which user you are logged in as
sudo <command>          # run a command as root (administrator)
```

### Handy shortcuts

| Shortcut | What it does |
|----------|-------------|
| `ctrl + c` | Stop the running program |
| `ctrl + z` | Pause the running program |
| `ctrl + d` | Log out / close the terminal |
| `ctrl + l` | Clear the screen |
| `tab` | Autocomplete a file or command name |
| `↑ / ↓` | Scroll through previous commands |
