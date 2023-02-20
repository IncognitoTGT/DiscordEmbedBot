# DiscordEmbedSender

### The entire thing, including the rest of the readme, was made using ChatGPT!

Embed Bot is a simple Discord bot that allows users to send rich embeds using slash commands.
# Usage
To use the bot, invite it to your Discord server using this link:

  [Invite](https://discord.com/api/oauth2/authorize?client_id=1074009731397595246&permissions=2733747207232&scope=bot)

Once the bot is in your server, you can send an embed by typing the following slash command:

	`/embed <title> <description> <color>`

Replace `<title>` with the title of your embed, `<description>` with the description of your embed, and `<color>` with the color of your embed. The `<color>` parameter must be one of the following options:
Red
Orange
Yellow
Green
Blue
Purple
White
Black
Here's an example of how to use the command:

`/embed "Hello, World!" "This is an example embed." Red`

## Development
If you want to modify or contribute to the Embed Bot, you can follow these steps:

	1. Clone this repository to your local machine.
	
	2. Install the required dependencies using `pip install -r requirements.txt.`.
	
	3. Create a new Discord application and bot account in the Discord Developer Portal.
	
	4. Obtain your bot's token from the Discord Developer Portal.
	
	5. Create a file named .env in the project directory, and add the following line:
	
	
```DISCORD_TOKEN=your-bot-token-here```

	6. Replace your-bot-token-here with your bot's token.

	7. Run the bot using `python3 bot.py`.

You can modify the code in bot.py to add new features or modify existing ones. Make sure to test your changes thoroughly before submitting a pull request.
## Credits
Embed Bot was created by ChatGPT with modifications by ma-ttp. It uses the following libraries:
`discord.py`,
`discord-py-slash-command`
## License
This project is licensed under the MIT License.
