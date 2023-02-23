#!/bin/bash

# Prompt the user for their bot token
read -p "Enter your bot token: " TOKEN

# Replace the placeholder string in the bot.py file with the token
sed -i "s/token_is_here/${TOKEN}/g" bot.py
