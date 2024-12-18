from vexsu import *
import keep_alive
import discord
import os

keep_alive.keep_alive()

bot = discord.Client()

p = ","

monitoring = {
    0: { 
        "channel_id": 1221040142869987440
    },
}

@bot.event
async def on_ready():
    clear()
    log("Connected", 3)

@bot.event
async def on_message(message):

    msg = message.content.lower()

    if message.author.id == bot.user.id: return
        
    if msg.startswith(f"{p}add"):
        args = msg.split(" ")
        monitoring[max(monitoring.keys(), default=-1) + 1] = {"channel_id": int(args[1])}
        log(f"Added {args[1]} to monitoring", 0)
    
    if message.author.bot: return
    for monitor in monitoring.values():
        if message.channel.id == monitor["channel_id"]:
            try:
                log(f"Recieved a message | {message.channel.id} - {message.author.id} > {message.id}", 3)
                webhook = discord.Webhook.from_url(os.environ.get('WEBHOOK'), client=bot)
                await webhook.send(message.content, username=message.author.name, avatar_url=message.author.avatar.url if message.author.avatar is not None else "https://cdn.discordapp.com/attachments/1277956788377096193/1318566959398387722/discord-avatar-512-8XW3B.png?ex=6762caac&is=6761792c&hm=2ee534535169008c69b3d7f002c806b40ba78c8528b623d1f2de516fad006adc&", files=message.attachments if message.attachments else [])
            except Exception as e:
                log(f"{e}", 2)



bot.run(os.environ.get('TOKEN'))
