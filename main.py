# botana-discord
import time
import discord
import requests
from discord.ext import tasks, commands
import random
import aiocron
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')
DISCORD_CHANNEL = os.environ.get('DISCORD_CHANNEL')
quote_api = os.environ.get('quote_api')
coin_api = os.environ.get('coin_api')
cat_api = os.environ.get('cat_api')
joke = os.environ.get('joke')
rapid_API = os.environ.get('rapid_API')
random_api = os.environ.get('random_api')
space_api = os.environ.get('space_api')
usnews_API = os.environ.get('usnews_API')
nznews_API = os.environ.get('nznews_API')
uknews_API = os.environ.get('uknews_API')
aunews_API = os.environ.get('aunews_API')


intents = discord.Intents.default()
intents.members=True
bot = discord.Client(intents=intents)



def say():
    hey = "Hello Mitielli, how you doing?"
    return hey

def quote():
    r = requests.get(quote_api)
    data = r.json()
    q = data[0]['q']
    a = data[0]['a']
    quote = (f'"{q}" \n-{a}')
    return quote

def pussy():
    r = requests.get(cat_api)
    data = r.json()
    url = data[0]['url']
    return url

def req_joke():
    headers = {
        'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
        'x-rapidapi-key': rapid_API
        }

    r = requests.request("GET",joke , headers=headers)
    data = r.json()
    j = data['body'][0]['setup']
    p = data['body'][0]['punchline']

    return j, p

def facts():
    r = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    data = r.json()
    before = data['text']
    fact = (f'Did you know\n{before}')
    return fact

def nasa_space():
    r = requests.get(space_api)
    data = r.json()
    body = data['explanation']
    img = data['url']
    return body, img

def usnews():
    r = requests.get(usnews_API)
    data = r.json()

    one = data['articles'][0]['url']
    two = data['articles'][1]['url']
    three = data['articles'][2]['url']
    four= data['articles'][3]['url']
    five = data['articles'][4]['url']
    six = data['articles'][5]['url']
     
    return one, two, three, four, five, six, 

def nznews():
    r = requests.get(nznews_API)
    data = r.json()

    one = data['articles'][0]['url']
    two = data['articles'][1]['url']
    three = data['articles'][2]['url']
    four= data['articles'][3]['url']
    five = data['articles'][4]['url']
    six = data['articles'][5]['url']
     
    return one, two, three, four, five, six, 

def uknews():
    r = requests.get(uknews_API)
    data = r.json()

    one = data['articles'][0]['url']
    two = data['articles'][1]['url']
    three = data['articles'][2]['url']
    four= data['articles'][3]['url']
    five = data['articles'][4]['url']
    six = data['articles'][5]['url']
     
    return one, two, three, four, five, six, 

def aunews():
    r = requests.get(aunews_API)
    data = r.json()

    one = data['articles'][0]['url']
    two = data['articles'][1]['url']
    three = data['articles'][2]['url']
    four= data['articles'][3]['url']
    five = data['articles'][4]['url']
    six = data['articles'][5]['url']
     
    return one, two, three, four, five, six, 

def Btc():
    r = requests.get(coin_api)
    data = r.json()
    
    s = data['data'][0]['symbol']
    n = data['data'][0]['name']
    r = data['data'][0]['rank']
    p = data['data'][0]['priceUsd']
    p_int = float(p)
    pnum = round(p_int, 2) 
    
    obj = s, n, r, pnum
    new = (f'{obj[1]} \n{obj[0]} \n${obj[3]} USD\nRank: {obj[2]}')
    return new

def Eth():
    r = requests.get(coin_api)
    data = r.json()
    
    s = data['data'][1]['symbol']
    n = data['data'][1]['name']
    r = data['data'][1]['rank']
    p = data['data'][1]['priceUsd']
    p_int = float(p)
    pnum = round(p_int, 2) 
          
    obj = s, n, r, pnum
    new = (f'{obj[1]} \n{obj[0]} \n${obj[3]} USD\nRank: {obj[2]}')
    return new

def Xrp():
    r = requests.get(coin_api)
    data = r.json()
    
    s = data['data'][5]['symbol']
    n = data['data'][5]['name']
    r = data['data'][5]['rank']
    p = data['data'][5]['priceUsd']
    p_int = float(p)
    pnum = round(p_int, 2) 
          
    obj = s, n, r, pnum
    new = (f'{obj[1]} \n{obj[0]} \n${obj[3]} USD\nRank: {obj[2]}')
    return new

def Sol():
    r = requests.get(coin_api)
    data = r.json()
    
    s = data['data'][6]['symbol']
    n = data['data'][6]['name']
    r = data['data'][6]['rank']
    p = data['data'][6]['priceUsd']
    p_int = float(p)
    pnum = round(p_int, 2) 
          
    obj = s, n, r, pnum
    new = (f'{obj[1]} \n{obj[0]} \n${obj[3]} USD\nRank: {obj[2]}')
    return new   



def main():
    
    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user.name}({bot.user.id})")
        await bot.change_presence(activity=discord.Game('online'))
        for guild in bot.guilds:
            if guild.name == 'familyGuy':
                break
        print(
            '****************************\n'
            f'{bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
            '****************************\n'
        )
        
    @bot.event
    async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(f'Hiya {member.name}! ')
        await member.dm_channel.send('Welcome to the Server!')
        await member.dm_channel.send('My name is Tink, I am currently still in beta, so any issues contact Admin.\nHere is list of commands to help you get started!')
        await member.dm_channel.send('- hi\n- hello\n- usnews\n- nznews\n- uknews\n- aunews\n- random\n- joke\n- pussy\n- btc\n- eth\n- xrp\n- sol\n- quote')
        await member.dm_channel.send('Enjoy your time here, have a great day! 😄')
    
    @bot.event
    async def on_message(message):
        username = str(message.author).split('#')[0]
        user_message =  str(message.content)
        #print(f'{username}: {user_message}')

        # don't respond to ourselves
        if message.author == bot.user:
            return
        
        if message.channel.name == 'general':
            if user_message.lower() == 'hi':
                hello = 'hi yourself'
                await message.channel.send(f'{hello}')
                return
        
        if message.channel.name == 'general':
            if user_message.lower() == 'hello':
                await message.channel.send(f'Why hello {username}! 💋')
                await message.channel.send(f'How can I help you?')
                return
           
        if message.channel.name == 'general':
            if user_message.lower() == 'hello':
                hello = 'hi yourself'
                await message.channel.send(f'{hello}')
                return
        
        if message.channel.name == 'general':
            if user_message.lower() == 'bye':
                await message.channel.send(f'Talk soon {username}!')
                return
        
        if message.channel.name == 'general':
            if user_message.lower() == 'btc':
                btc = Btc()
                await message.channel.send(f'\n{btc} \n')
                return
            elif user_message.lower() == 'eth':
                eth = Eth()
                await message.channel.send(f'\n{eth} \n')
                return
            elif user_message.lower() == 'xrp':
                xrp = Xrp()
                await message.channel.send(f'\n{xrp} \n')
                return
            elif user_message.lower() == 'sol':
                sol = Sol()
                await message.channel.send(f'\n{sol} \n')
                return
        
        if message.channel.name == 'general':
            if user_message.lower() == 'quote':
                saying = quote()
                await message.channel.send(f'@everyone \n{saying}\n')
                return

        if message.channel.name == 'general':
            if user_message.lower() == 'pussy':
                cat = pussy()
                await message.channel.send(f'Ill show you some pussy')
                time.sleep(1)
                await message.channel.send(f'{cat}')
                time.sleep(2)
                await message.channel.send(f'Yeah, you like that? You dirty bastard')
                return

        if message.channel.name == 'general':
            if user_message.lower() == 'joke':
                joke, punch = req_joke()
                line = ['I did hear this one the other day', 'Now let me try rememeber', 'I just heard this funny', 'Oh! Oh! I got one', 'Now do I have a joke for you', 'I am so glad you asked!', 'This one made me LAUGH']
                react = ['🤣', '🤣 🤣', '😉', 'hahaha', 'LOL', 'Trust me, I know!\nI crack myself up!', 'What a hoot!', 'haha', '😂', '🤪 😂']
                emoj = random.choice(react)
                pre = random.choice(line)
                await message.channel.send(pre)
                time.sleep(2)
                await message.channel.send(joke)
                time.sleep(4)
                await message.channel.send(f'\n {punch}')
                time.sleep(2)
                await message.channel.send(emoj)
                return
        
        if message.channel.name == 'general':
            if user_message.lower() == 'random':
                randfact = facts()
                await message.channel.send(f'@everyone \n{randfact}\n')
        
        if user_message.lower() == 'space':
            space, blob = nasa_space()
            time.sleep(2)
            await message.channel.send(f'{space}')
            time.sleep(3)
            await message.channel.send(f'{blob}')
            return       

        if message.channel.name == 'general':
            if user_message.lower() == 'usnews':
                one, two, three, four, five, six = usnews()
                await message.channel.send(f'@everyone \n* US News Update *\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{one}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{two}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{three}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{four}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{five}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{six}\n')
        
        if message.channel.name == 'general':
            if user_message.lower() == 'nznews':
                one, two, three, four, five, six = nznews()
                await message.channel.send(f'@everyone \n* NZ News Update *\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{one}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{two}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{three}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{four}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{five}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{six}\n')
        
        if message.channel.name == 'general':
            if user_message.lower() == 'uknews':
                one, two, three, four, five, six = uknews()
                await message.channel.send(f'@everyone \n* UK News Update *\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{one}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{two}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{three}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{four}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{five}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{six}\n')
                
        if message.channel.name == 'general':
            if user_message.lower() == 'aunews':
                one, two, three, four, five, six = aunews()
                await message.channel.send(f'@everyone \n* Aus News Update *\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{one}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{two}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{three}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{four}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{five}\n')
                time.sleep(2)
                await message.channel.send(f'@everyone \n{six}\n')    
    
    
    @aiocron.crontab('30 6 * * *')
    async def morning_news():
        await bot.wait_until_ready()
        channel = bot.get_channel(int(DISCORD_CHANNEL))
        country, one, two, three, four, five, six = nznews()
        await channel.send(f'@everyone {country}')
        await channel.send(f'@everyone {country}')
        time.sleep(2)
        await channel.send(f'@everyone {one}')
        time.sleep(2)
        await channel.send(f'@everyone {two}') 
        time.sleep(2)
        await channel.send(f'@everyone {three}')
        time.sleep(2)
        await channel.send(f'@everyone {four}')
        time.sleep(2)
        await channel.send(f'@everyone {five}')
        time.sleep(2)
        await channel.send(f'@everyone {six}')
        
    @aiocron.crontab('0 13 * * *')
    async def arvo_news():
        await bot.wait_until_ready()
        channel = bot.get_channel(int(DISCORD_CHANNEL))
        country, one, two, three, four, five, six = aunews()
        await channel.send(f'@everyone {country}')
        await channel.send(f'@everyone {country}')
        time.sleep(2)
        await channel.send(f'@everyone {one}')
        time.sleep(2)
        await channel.send(f'@everyone {two}') 
        time.sleep(2)
        await channel.send(f'@everyone {three}')
        time.sleep(2)
        await channel.send(f'@everyone {four}')
        time.sleep(2)
        await channel.send(f'@everyone {five}')
        time.sleep(2)
        await channel.send(f'@everyone {six}')
        
    @aiocron.crontab('0 18 * * *')
    async def night_news():
        await bot.wait_until_ready()
        channel = bot.get_channel(int(DISCORD_CHANNEL))
        country, one, two, three, four, five, six = usnews()
        await channel.send(f'@everyone {country}')
        await channel.send(f'@everyone {country}')
        time.sleep(2)
        await channel.send(f'@everyone {one}')
        time.sleep(2)
        await channel.send(f'@everyone {two}') 
        time.sleep(2)
        await channel.send(f'@everyone {three}')
        time.sleep(2)
        await channel.send(f'@everyone {four}')
        time.sleep(2)
        await channel.send(f'@everyone {five}')
        time.sleep(2)
        await channel.send(f'@everyone {six}')
        
    @aiocron.crontab('0 10 * * *')
    async def morning_joke():
        await bot.wait_until_ready()
        channel = bot.get_channel(int(DISCORD_CHANNEL))
        joke, punch = req_joke()
        line = ['I think its time for a laugh!', 'Whose needs a smile on their face?!', 'I just heard this funny', 'Oh! Oh! I have something funny to say', 'Now do I have a joke for you', 'Listen to this', 'Here is something that will you LAUGH']
        react = ['🤣', '🤣 🤣', '😉', 'hahaha', 'LOL', 'Trust me, I know!\nI crack myself up!', 'What a hoot!', 'haha', '😂', '🤪 😂', 'honestly 🤣' ]
        emoj = random.choice(react)
        pre = random.choice(line)
        await channel.send(pre)
        time.sleep(2)
        await channel.send(joke)
        time.sleep(4)
        await channel.send(f'\n {punch}')
        time.sleep(2)
        await channel.send(emoj)
        return
        
    @aiocron.crontab('0 12 * * *')
    async def crypto():
        await bot.wait_until_ready()
        channel = bot.get_channel(int(DISCORD_CHANNEL))
        btc = Btc()
        eth = Eth()
        xrp = Xrp()
        sol = Sol()
        await channel.send('* Midday Crypto Update *')
        time.sleep(2)
        await channel.send(btc)
        time.sleep(2)
        await channel.send(eth)
        time.sleep(4)
        await channel.send(xrp)
        time.sleep(2)
        await channel.send(sol)
    
    @aiocron.crontab('0 15 * * *')
    async def arvo_fact():
        await bot.wait_until_ready()
        channel = bot.get_channel(int(DISCORD_CHANNEL))
        line = ['Who wants to get some knowledge?!', 'Would anyone like to learn something?', 'Its a `did you know moment!`\nDid you know that', 'I just learnt something today', 'Interesting fact: ', 'I just never knew this', 'Ready for some brand new information!?']
        randfact = facts()
        first = random.choice(line)
        await channel.send(f'@everyone\n{first}')
        time.sleep(2)
        await channel.send(f'@everyone\n{randfact}\n')
    
    @aiocron.crontab('* * * * *')
    async def greeting():
        channel = bot.get_channel(int(DISCORD_CHANNEL))
        hello = "Testing 1 2 3"
        await channel.send(f'@everyone {hello}')

    
    bot.run(DISCORD_TOKEN)
    bot.loop.create_task(morning_news())
    bot.loop.create_task(arvo_news())
    bot.loop.create_task(night_news())
    bot.loop.create_task(morning_joke())
    bot.loop.create_task(crypto())
    bot.loop.create_task(arvo_fact())
    bot.loop.create_task(greeting())
    
    
    

main()
