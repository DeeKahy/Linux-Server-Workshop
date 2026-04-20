#!/bin/bash

# What folder do you want to back up?
SOURCE="$HOME/server-workshop"

# Where should backups go?
BACKUP_DIR="$HOME/backups"

# Create the backup folder if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Build a filename with today's date and time
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/backup_$TIMESTAMP.tar.gz"

echo "Backing up: $SOURCE"
echo "Saving to:  $BACKUP_FILE"

# tar = create an archive, -czf = compress it
tar -czf "$BACKUP_FILE" "$SOURCE"

# Check if the backup worked
if [ $? -eq 0 ]; then
    SIZE=$(du -sh "$BACKUP_FILE" | cut -f1)
    echo ""
    echo "Done! Backup size: $SIZE"
else
    echo ""
    echo "Something went wrong."
fi

echo ""
echo "All backups:"
ls -lh "$BACKUP_DIR"
