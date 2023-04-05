import discord
import responses
import os
from dotenv import load_dotenv

async def send_message(message, user_message, is_private):
    try: 
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception:
        print(Exception)


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    load_dotenv()
    TOKEN = os.getenv('BOT_TOKEN')
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        #don't respond to your own messages
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        #debug
        print(f'{username} : wrote {user_message} | in {channel}')

        if user_message[0] == '!':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=False)
        elif user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            return


    client.run(TOKEN)