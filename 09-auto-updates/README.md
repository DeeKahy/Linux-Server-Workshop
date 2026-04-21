# 10 - Automatic Security Updates

One of the most important things you can do for any server is **keep it updated**. Most real-world breaches happen because someone was running old software with known vulnerabilities - vulnerabilities that had already been patched.

The problem: manually running `apt update && apt upgrade` every day is tedious and people forget.

The solution: **unattended-upgrades** - a tool that automatically installs security patches in the background, without you doing anything.

---

## How apt works (quick background)

Ubuntu uses **apt** to install and update software:

```bash
sudo apt update            # refresh the list of available packages
sudo apt upgrade           # install all available upgrades
sudo apt install <package> # install a specific package
sudo apt remove <package>  # remove a package
sudo apt autoremove        # clean up packages no longer needed
```

`unattended-upgrades` automates the security-update part of this on a daily schedule.

---

## Step 1 - Install unattended-upgrades

```bash
sudo apt update
sudo apt install -y unattended-upgrades
```

It may already be installed on Ubuntu - that's fine.

---

## Step 2 - Copy the config files

This project includes two config files with sensible defaults. Copy them into place:

```bash
sudo cp 50unattended-upgrades /etc/apt/apt.conf.d/50unattended-upgrades
sudo cp 20auto-upgrades /etc/apt/apt.conf.d/20auto-upgrades
```

Have a look at what's in them:

```bash
cat /etc/apt/apt.conf.d/50unattended-upgrades
cat /etc/apt/apt.conf.d/20auto-upgrades
```

**What `50unattended-upgrades` controls:**
- Which updates to install automatically (security only, not everything)
- Whether to clean up unused packages after upgrading
- Whether to auto-reboot (set to `false` - you don't want surprise reboots)

**What `20auto-upgrades` controls:**
- How often each step runs (the `"1"` values mean once per day)

---

## Step 3 - Enable and start the service

```bash
sudo systemctl enable unattended-upgrades
sudo systemctl start unattended-upgrades
sudo systemctl status unattended-upgrades
```

You should see `active (running)`.

---

## Step 4 - Do a dry run to verify it works

This simulates the process without actually installing anything:

```bash
sudo unattended-upgrades --dry-run --debug
```

Read through the output - it will list what it would install and why.

---

## Check the logs later

After the service has been running, logs appear here:

```bash
cat /var/log/unattended-upgrades/unattended-upgrades.log
```

---

## Manual updates still matter

Unattended-upgrades only covers **security patches**. For everything else, still run this occasionally:

```bash
sudo apt update && sudo apt upgrade
```

---

## Quick reference

| Command | What it does |
|---------|-------------|
| `sudo apt update` | Refresh the package list |
| `sudo apt upgrade` | Install all available upgrades |
| `sudo apt install <pkg>` | Install a package |
| `sudo apt remove <pkg>` | Remove a package |
| `sudo apt autoremove` | Remove packages no longer needed |
| `sudo apt list --upgradable` | Show what's currently out of date |
| `sudo unattended-upgrades --dry-run` | Test without installing anything |

