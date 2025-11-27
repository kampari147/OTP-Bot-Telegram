#!/usr/bin/env python3
"""Minimal, safe Telegram bot for local testing.

Features:
- /start: greeting
- /help: small help text

This file intentionally avoids any obfuscated code or external services.
It reads the bot token from the BOT_TOKEN environment variable.
"""
import os
import telebot


def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("ERROR: BOT_TOKEN environment variable is not set.")
        print("Set it with: export BOT_TOKEN=\"<your_token>\" and run this script again.")
        return

    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start(message):
        bot.reply_to(message, "Hello! This is a safe demo bot. Use /help to see commands.")

    @bot.message_handler(commands=["help"])
    def help_cmd(message):
        help_text = (
            "Available commands:\n"
            "/start - Greet the bot\n"
            "/help - Show this message"
        )
        bot.reply_to(message, help_text)

    @bot.message_handler(commands=["ping"])
    def ping(message):
        bot.reply_to(message, "pong")

    @bot.message_handler(commands=["echo"])
    def echo(message):
        # /echo some text -> replies with 'some text'
        parts = message.text.split(' ', 1)
        if len(parts) == 1 or not parts[1].strip():
            bot.reply_to(message, "Usage: /echo your message")
            return
        bot.reply_to(message, parts[1])

    print("Safe bot started. Listening for messages (press Ctrl+C to stop).")
    bot.infinity_polling()


if __name__ == "__main__":
    main()
