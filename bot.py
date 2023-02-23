import discord
from discord.ext import commands

# Define bot prefix
bot_prefix = "+"

# Create bot client
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='+', intents=intents)
# Set up color picker reaction options
color_emojis = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪"]
color_map = {
    "🟥": discord.Color.red(),
    "🟧": discord.Color.orange(),
    "🟨": discord.Color.gold(),
    "🟩": discord.Color.green(),
    "🟦": discord.Color.blue(),
    "🟪": discord.Color.purple(),
}

# Define embed builder command
@bot.command()
async def embed(ctx):
    # Define initial embed with default values
    embed = discord.Embed(title="Title", description="Description", color=discord.Color.blue())

    # Send initial embed message and add color picker reactions
    embed_message = await ctx.send(embed=embed)
    for emoji in color_emojis:
        await embed_message.add_reaction(emoji)

    # Define reaction check function
    def reaction_check(reaction, user):
        return (
            user == ctx.author
            and reaction.message.id == embed_message.id
            and reaction.emoji in color_emojis
        )

    # Wait for user to select color
    reaction, _ = await bot.wait_for("reaction_add", check=reaction_check)

    # Set embed color based on selected emoji
    selected_color = color_map[reaction.emoji]
    embed.color = selected_color

    # Ask user for title and description inputs
    await ctx.send("What would you like the title to be?")
    title_message = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
    embed.title = title_message.content
    await title_message.delete()

    await ctx.send("What would you like the description to be?")
    description_message = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
    embed.description = description_message.content
    await description_message.delete()

    # Ask user if they want to add an image
    await ctx.send("Would you like to include an image? (y/n)")
    image_message = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
    if image_message.content.lower() == "y":
        await ctx.send("Please provide the image URL.")
        image_url_message = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
        embed.set_image(url=image_url_message.content)
        await image_url_message.delete()

    # Ask user if they want to add a link
    await ctx.send("Would you like to include a link? (y/n)")
    link_message = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
    if link_message.content.lower() == "y":
        await ctx.send("Please provide the link URL.")
        link_url_message = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
        embed.url = link_url_message.content
        await link_url_message.delete()

    # Remove color picker reactions
    for emoji in color_emojis:
        await embed_message.remove_reaction(emoji, bot.user)

    # Update embed message with user's choices
    await embed_message.edit(embed=embed)

    # Delete bot's messages
    await ctx.channel.purge(limit=6)

# Run bot with your bot token
bot.run("token is here")

