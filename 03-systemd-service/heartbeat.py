import time
import datetime

LOG_FILE = "/tmp/heartbeat.log"

print("Heartbeat service started!")

while True:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{now}] Still running...\n"

    print(message, end="")

    with open(LOG_FILE, "a") as f:
        f.write(message)

    time.sleep(5)
