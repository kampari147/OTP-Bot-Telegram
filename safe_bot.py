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

    @bot.message_handler(commands=["time"])
    def time_cmd(message):
        from datetime import datetime
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        bot.reply_to(message, f"Current server time: {current_time}")

    @bot.message_handler(commands=["status"])
    def status_cmd(message):
        bot.reply_to(message, "🟢 Bot is online and healthy!")

    @bot.message_handler(commands=["info"])
    def info_cmd(message):
        info_text = (
            "📋 Safe Demo Bot Info:\n"
            "Version: 1.0\n"
            "Status: Active\n"
            "Purpose: Safe testing of Telegram bot functionality\n"
            "No external APIs or malicious code."
        )
        bot.reply_to(message, info_text)

    @bot.message_handler(func=lambda message: True)
    def default_handler(message):
        # Catch-all for any text message not matched by other handlers
        bot.reply_to(
            message,
            "Unknown command. Send /help to see available commands."
        )

    print("Safe bot started. Listening for messages (press Ctrl+C to stop).")
    bot.infinity_polling()


if __name__ == "__main__":
    main()
