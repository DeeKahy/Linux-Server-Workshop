# 05 — Bash Scripting

A bash script is just a text file full of commands — the same commands you type in the terminal, saved so you can run them all at once. Bash scripts are everywhere in server work: backups, deployments, health checks, automation.

This project has three scripts, each teaching something new.

---

## Before you start — make scripts executable

Linux won't run a script unless you tell it the file is allowed to be executed:

```bash
cd 05-bash-scripting
chmod +x 01_hello.sh 02_system_info.sh 03_backup.sh
```

You only need to do this once per file.

---

## Script 1 — Variables and input

```bash
./01_hello.sh
```

**What it teaches:** Variables (`NAME="World"`), printing with `echo`, and reading user input with `read`.

Open it and have a look:
```bash
nano 01_hello.sh
```

**Key things to notice:**
- Variables are set with `NAME="value"` — no spaces around `=`
- Variables are used with a `$` in front: `$NAME`
- `read YOUR_NAME` waits for the user to type something

---

## Script 2 — System info

```bash
./02_system_info.sh
```

**What it teaches:** Running commands inside a script, using `$(command)` to put command output into a variable.

This script shows you:
- Who is logged into the server right now
- How much disk space is left
- How much memory is in use
- Which processes are using the most CPU

**Key thing to notice:** `$(hostname)` runs the `hostname` command and drops its output right into the `echo`.

---

## Script 3 — Backup with a timestamp

```bash
./03_backup.sh
```

**What it teaches:** `if` statements, creating folders, archiving files, checking if a command succeeded.

This script compresses your entire `server-workshop` folder into a `.tar.gz` file (like a zip) and names it with the current date and time. Run it a few times and you'll see multiple backups appear.

**Key things to notice:**
- `mkdir -p` creates a folder (and doesn't error if it already exists)
- `if [ $? -eq 0 ]` checks whether the last command succeeded (`$?` is the exit code — `0` means OK)
- `tar -czf` creates a compressed archive

---

## Challenge ideas

- Edit `03_backup.sh` to delete backups older than 3 files (hint: look up `ls | head` and `rm`)
- Add a check to `02_system_info.sh` that prints a warning if disk usage is above 80%
- Write your own script from scratch that counts how many `.py` files are in the repo (hint: `find . -name "*.py" | wc -l`)
- Add a loop: `for i in 1 2 3 4 5; do echo "Number $i"; done`
