# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from search import google_search
from dataBase import get_search_data, post_search_data
load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = {'DISCORD_TOKEN'}
GUILD = {'SERVER_NAME'}

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    user_id = message.author.id
    msg = message.content.lower()
    if message.author == client.user:
        return

    if  msg.startswith('hi'):
        response = 'Hey'
        await message.channel.send(response)

    if msg.startswith('!google'):
        msg = msg.split(None, 1)[1]
        post_search_data(user_id, msg)
        response = google_search(msg, user_id)
        if response:
            response = 'Result of search: {}'.format(response)

        else:
            response = 'Your search - {} - did not match any documents.'.format(msg)
        await message.channel.send(response)

    if msg.startswith('!recent'):
        msg = msg.split(None, 1)[1]
        response = get_search_data(user_id,msg)
        if response:
            response = 'Result of search: {}' .format(response)

        else:
            response = 'Your search - {} - did not match any documents.'.format(msg)
        await message.channel.send(response)

client.run(TOKEN)

