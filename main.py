import discord
import requests
import json
import random

client = discord.Client()

sad_words = ["sad", "depressed", "плохо", "эхх", "грустно","депрессия"]
starter_encouragements = [
  "Всё будет хорошо",
  "Подними голову выше",
  "Не расстраивайся!"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    if message.content.startswith('$hello'):
        await message.channel.send('Hello world!!')
    if message.content.startswith('$help'):
        await message.channel.send('Сори, но я пока туп, команд нету')
    if message.content.startswith('Всем привет'):
        await message.channel.send('привет :dionarawr: ')
    msg = message.content
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))



client.run('OTA4NzQyNDgwNzI2NDkxMTU3.YY6KYw.GYDOg8iYnb_v0qtDD29f5tT3cd4')
