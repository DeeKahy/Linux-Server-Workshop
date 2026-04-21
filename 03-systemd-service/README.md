# 03 - systemd Service

So far, every program you've run stops when you close the terminal. **systemd** is the tool Linux uses to run programs as proper background services - they start automatically on boot and restart if they crash.

This project runs a tiny script called `heartbeat.py` that writes a log every 5 seconds. You'll turn it into a service.

---

## Step 1 - Run it manually first

```bash
cd 03-systemd-service
python3 heartbeat.py
```

You'll see it printing every 5 seconds. Press `ctrl+c` to stop it.

It also writes to `/tmp/heartbeat.log`. Check that file:
```bash
cat /tmp/heartbeat.log
```

---

## Step 2 - Edit the service file

Open `heartbeat.service` and update the path on the `ExecStart` line to match where you cloned the repo:

```bash
nano heartbeat.service
```

Change:
```
ExecStart=/usr/bin/python3 /home/ubuntu/server-workshop/03-systemd-service/heartbeat.py
```

If you cloned somewhere else, adjust the path. Save with `ctrl+o` then `ctrl+x`.

---

## Step 3 - Install the service

Copy the service file to where systemd looks for services:

```bash
sudo cp heartbeat.service /etc/systemd/system/heartbeat.service
```

Tell systemd to pick up the new file:
```bash
sudo systemctl daemon-reload
```

---

## Step 4 - Start it

```bash
sudo systemctl start heartbeat
```

Check that it's running:
```bash
sudo systemctl status heartbeat
```

You should see `active (running)` in green.

---

## Step 5 - Watch the logs

```bash
# Watch the log file update live
tail -f /tmp/heartbeat.log

# Or use journalctl to see systemd's logs
sudo journalctl -u heartbeat -f
```

Press `ctrl+c` to stop watching.

---

## Step 6 - Make it start on boot

```bash
sudo systemctl enable heartbeat
```

Now it will survive a reboot.

---

## Useful commands

| Command | What it does |
|---------|--------------|
| `sudo systemctl start heartbeat` | Start the service |
| `sudo systemctl stop heartbeat` | Stop the service |
| `sudo systemctl restart heartbeat` | Restart it |
| `sudo systemctl status heartbeat` | See if it's running |
| `sudo systemctl enable heartbeat` | Start on boot |
| `sudo systemctl disable heartbeat` | Don't start on boot |

---

## Challenge ideas

- Edit `heartbeat.py` to log something different, then restart the service and watch it change
- Make the service restart automatically after a crash - look up `Restart=on-failure` in the service file
- Try stopping the process manually (`sudo kill <pid>`) and watch systemd bring it back
