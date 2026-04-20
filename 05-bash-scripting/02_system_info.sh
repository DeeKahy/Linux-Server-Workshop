#!/bin/bash

echo "============================="
echo "  Server Info"
echo "============================="

echo ""
echo "Hostname:   $(hostname)"
echo "Uptime:     $(uptime -p)"
echo "Date/Time:  $(date)"

echo ""
echo "--- Disk Space ---"
df -h /

echo ""
echo "--- Memory ---"
free -h

echo ""
echo "--- Who's logged in ---"
who

echo ""
echo "--- Last 5 running processes ---"
ps aux --sort=-%cpu | head -6
