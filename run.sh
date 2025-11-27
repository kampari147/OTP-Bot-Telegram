#!/usr/bin/env bash
# Helper script to run the bot locally.
# Prompts for BOT_TOKEN if not already set in the environment.

set -euo pipefail

if [ -z "${BOT_TOKEN:-}" ]; then
  echo "BOT_TOKEN not set in environment."
  read -s -p "Enter BOT_TOKEN (input hidden): " ENTERED
  echo
  if [ -z "$ENTERED" ]; then
    echo "No token provided. Exiting." >&2
    exit 1
  fi
  export BOT_TOKEN="$ENTERED"
fi

echo "Starting bot..."
python3 bot.py
