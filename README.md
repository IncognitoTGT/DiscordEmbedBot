# DiscordEmbedSender

![logo](/logo.png)



DiscordEmbed sender is a simple Discord bot that can be used to send embeds. [Invite](https://discord.com/api/oauth2/authorize?client_id=1074009731397595246&permissions=8&scope=bot%20applications.commands)

To start, just type `+embed` and it'll walk you through!

# Self-hosting

To self host, make sure that you have pip3. Once you do, clone the repo (`git clone https://github.com/ma-ttp/DiscordEmbedSender`). Then, do the following things: 

On Mac, run `swift setup.swift` in a terminal.
On Windows, click `setup.bat` in a terminal.
Linux users are smart enough (yes I do know how to use it so no bashing)

Enter your bot token, and it's setup!

To run it, enter `python3 bot.py` in a terminal.

## Advanced options

### Status

You can change your bot's status simply by modifying the line of code below (on line 15):

```python
await bot.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.listening, name="+embed"))
```

Modify `status=discord.Status.online` to something such as `status=discord.Status.idle`. See [here](https://dev.to/tejasdev/adding-discord-bot-status-with-python-a2a) for more.

Also, you can change `name="+embed"))` to another status. 

### Prefix

Change the following 2 lines to the new prefix, along with the status.

(line 6)

```python
# Define bot prefix
bot_prefix = "+"
```
and (line 10)

```python
# Create bot client
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='+', intents=intents)
```


 

