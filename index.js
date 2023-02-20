const fs = require('fs');
const Discord = require('discord.js');
const { REST } = require('@discordjs/rest');
const { Routes } = require('discord-api-types/v9');

const config = JSON.parse(fs.readFileSync('./config.json', 'utf-8'));

const client = new Discord.Client({
  intents: [Discord.Intents.FLAGS.GUILDS, Discord.Intents.FLAGS.GUILD_MESSAGES]
});

client.once('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('interactionCreate', async interaction => {
  if (!interaction.isCommand()) return;

  const { commandName } = interaction;

  if (commandName === 'embed') {
    const title = interaction.options.getString('title');
    const description = interaction.options.getString('description');
    const color = interaction.options.getString('color');
    
    const embed = new Discord.MessageEmbed()
      .setTitle(title)
      .setDescription(description)
      .setColor(color);

    await interaction.reply({ embeds: [embed] });
  }
});

const rest = new REST({ version: '9' }).setToken(config.token);

(async () => {
  try {
    console.log('Started refreshing application (/) commands.');

    await rest.put(
      Routes.applicationCommands(config.clientId),
      { body: [
        {
          name: 'embed',
          description: 'Send an embed with a title and description',
          options: [
            {
              name: 'title',
              description: 'The title of the embed',
              type: 'STRING',
              required: true
            },
            {
              name: 'description',
              description: 'The description of the embed',
              type: 'STRING',
              required: true
            },
            {
              name: 'color',
              description: 'The color of the embed (in hex code or integer form)',
              type: 'STRING',
              required: false
            }
          ]
        }
      ]},
    );

    console.log('Successfully reloaded application (/) commands.');
  } catch (error) {
    console.error(error);
  }
})();

client.login(config.token);
