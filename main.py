#!/usr/bin/env python3
from asyncio import sleep
import discord

from dexscreener import DexscreenerClient

BOT_TOKEN = 'OTM5OTI1OTUzNjQ2MzA5NDE4.Yf_8Qg.KAL9wScBMaMbVqcFotUcxEHpJk0'
INTERVAL = 1

discord_client = discord.Client()
dex_client = DexscreenerClient()

prev_price = float(0.0)

async def push_update():
    history = dex_client.recent_trade_history("fantom", "0x937813380c7b98a66afa5992bf2231e3e5913ef4")
    most_recent = history.trade_history[0]
    price = most_recent.price_usd

    global prev_price
    if price == prev_price:
        return
    prev_price = price

    for guild in discord_client.guilds:
        await guild.me.edit(nick=f"Rich @ USD%.3f"%price)

@discord_client.event
async def on_ready():
    while True:
        try:
            await sleep(INTERVAL)
            await push_update()
        except:
            continue

if __name__ == "__main__":
    discord_client.run(BOT_TOKEN)
