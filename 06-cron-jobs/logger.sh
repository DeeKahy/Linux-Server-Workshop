#!/bin/bash

LOG_FILE="$HOME/cron_log.txt"

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Cron job ran" >> "$LOG_FILE"
