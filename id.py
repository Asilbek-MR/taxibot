from telethon import TelegramClient

# Telegram API ma'lumotlari

api_id = '26230342'  
api_hash = '9ae7a9067e358b1cbae12ac0a20ff95e'  
bot_token = '8069163980:AAFt1uZivsOenc6Gr_N0uhD6itX_1-RGWRE'

client = TelegramClient('session', api_id, api_hash)

async def get_group_id():
    async for dialog in client.iter_dialogs():
        print(f"Chat: {dialog.name}, ID: {dialog.id}")

with client:
    client.loop.run_until_complete(get_group_id())
