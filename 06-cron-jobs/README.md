# 06 - Cron Jobs

In the systemd project you made a service that runs *constantly*. Sometimes you don't want that - you just want something to run **at a specific time**, like "every day at midnight" or "every 5 minutes".

That's what **cron** is for. It's a scheduler built into every Linux system.

---

## Step 1 - Try the script manually

```bash
cd 06-cron-jobs
chmod +x logger.sh
./logger.sh
```

Check the log file it created:
```bash
cat ~/cron_log.txt
```

Run it a few more times and watch the file grow.

---

## Step 2 - Schedule it with cron

Open your crontab (your personal cron schedule):

```bash
crontab -e
```

This opens a text editor. Add this line at the bottom:

```
* * * * * /home/ubuntu/server-workshop/06-cron-jobs/logger.sh
```

Save and exit (`ctrl+o`, `ctrl+x` for nano).

This runs the script **every minute**.

---

## Step 3 - Watch it run

Wait a minute or two, then check the log:

```bash
cat ~/cron_log.txt
```

You should see new entries appearing. Or watch it live:

```bash
watch cat ~/cron_log.txt
```

(`ctrl+c` to stop)

---

## Understanding the cron schedule

The `* * * * *` at the start is a time pattern. There are 5 slots:

```
┌───────── minute        (0–59)
│ ┌─────── hour          (0–23)
│ │ ┌───── day of month  (1–31)
│ │ │ ┌─── month         (1–12)
│ │ │ │ ┌─ day of week   (0=Sun, 6=Sat)
│ │ │ │ │
* * * * *   ← every minute of every day
```

### Examples

| Schedule | Meaning |
|----------|---------|
| `* * * * *` | Every minute |
| `*/5 * * * *` | Every 5 minutes |
| `0 * * * *` | Every hour (at :00) |
| `0 9 * * *` | Every day at 9am |
| `0 9 * * 1` | Every Monday at 9am |
| `0 0 1 * *` | First day of every month at midnight |

---

## Useful cron commands

```bash
crontab -l          # list your current cron jobs
crontab -e          # edit your cron jobs
crontab -r          # remove ALL your cron jobs (careful!)
```

---

## Challenge ideas

- Change the schedule to run every 2 minutes (`*/2 * * * *`)
- Edit `logger.sh` to also log disk usage (hint: `df -h / | tail -1`)
- Schedule the backup script from project 05 to run once a day
- Add a second cron job that does something different
