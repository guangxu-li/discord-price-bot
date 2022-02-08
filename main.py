#!/usr/bin/env python3
from asyncio import sleep
import discord

from dexscreener import DexscreenerClient

BOT_TOKEN = 'OTM5OTI1OTUzNjQ2MzA5NDE4.Yf_8Qg.KAL9wScBMaMbVqcFotUcxEHpJk0'
INTERVAL = 5

discord_client = discord.Client()
dex_client = DexscreenerClient()

async def push_update():
    for guild in discord_client.guilds:
        history = dex_client.recent_trade_history("fantom", "0x937813380c7b98a66afa5992bf2231e3e5913ef4")
        most_recent = history.trade_history[0]
        price = most_recent.price_usd

        await guild.me.edit(nick=f"Rich @ USD%.2f"%price)

@discord_client.event
async def on_ready():
    while True:
        await push_update()
        await sleep(INTERVAL)

if __name__ == "__main__":
    discord_client.run(BOT_TOKEN)
