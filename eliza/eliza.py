import chatbot
import discord

class Eliza:

    def __init__(self, token, channel):
        self.token = token
        self.channel = channel
        self.discord_bot = discord.AutoShardedClient()
        self.setup_discord_events()

    def setup_discord_events(self):

        @self.discord_bot.event
        async def on_ready():
            print('ELIZA has connected to Discord!')

        @self.discord_bot.event
        async def on_message(message):

            if message.author.bot or str(message.channel) != self.channel:
                return

            text = message.content
            for ch in ['/', "'", ".", "\\", "(", ")", '"', '\n', '@', '<', '>']:
                text = text.replace(ch, '')
            response = chatbot.respond(text)
            await message.channel.send(response)

    def run(self):
        self.discord_bot.run(self.token)

# set up virtual environment

# 3/28/20: Needed to reinstall textblob and discord.py