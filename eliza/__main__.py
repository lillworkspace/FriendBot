import os
from dotenv import load_dotenv
from eliza import Eliza

def main():

    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    channel = os.getenv('DISCORD_CHANNEL')

    bot = Eliza(token, channel)
    bot.run()

if __name__ == '__main__':
    main()