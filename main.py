from telethon import TelegramClient, events

# bot_username = '@appealuserbot'
# CHANNEL_USERNAME = enginer_developer
# ADMIN_CHANNEL_ID = -1001518206463
# Bot va API ma'lumotlari
api_id = '26230342'  # Telegram API ID
api_hash = '9ae7a9067e358b1cbae12ac0a20ff95e'  # Telegram API Hash
bot_token = '7129894107:AAFvR_xicYQ0S7viH4K0usQemKDGmQYLZa0'  # Bot token
channel_username = '@every_dev'  # Kanalingiz username (masalan, '@kanalim')

# TelegramClient ob'ekti yaratish
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# Foydalanuvchi ma'lumotlarini saqlash uchun dict
user_data = {}

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond("Assalomu alaykum!")

    # Keyingi xabar uchun get_name funksiyasini kutadi
    client.add_event_handler(get_name, events.NewMessage(from_users=event.sender_id))

async def get_name(event):
    name = event.text.strip()
    if name:
        user_data[event.sender_id] = {"name": name}  # Ismni saqlash
        await event.respond("Hush kelibsiz! Ismingizni kiriting: Qayerga borasiz? Manzilingizni kiriting:")

        # Keyingi xabar uchun get_destination funksiyasini kutadi
        client.add_event_handler(get_destination, events.NewMessage(from_users=event.sender_id))

        # get_name funksiyasini o'chiradi
        client.remove_event_handler(get_name, events.NewMessage(from_users=event.sender_id))
    else:
        await event.respond("Iltimos, ismingizni kiriting:")

async def get_destination(event):
    destination = event.text.strip()
    if destination:
        user_data[event.sender_id]["destination"] = destination  # Manzilni saqlash
        await event.respond("Telefon raqamingizni kiriting (+998...) yoki uni ulashing:")

        # Keyingi xabar uchun get_phone funksiyasini kutadi
        client.add_event_handler(get_phone, events.NewMessage(from_users=event.sender_id))

        # get_destination funksiyasini o'chiradi
        client.remove_event_handler(get_destination, events.NewMessage(from_users=event.sender_id))
    else:
        await event.respond("Iltimos, manzilingizni kiriting:")

async def get_phone(event):
    phone = event.text.strip()
    if phone:
        user_data[event.sender_id]["phone"] = phone  # Telefon raqamini saqlash

        # Ma'lumotlarni kanalga yuborish
        message = (f"Yangi foydalanuvchi:\n"
                   f"Ismi: {user_data[event.sender_id]['name']}\n"
                   f"Manzili: {user_data[event.sender_id]['destination']}\n"
                   f"Telefon raqami: {phone}")
        await client.send_message(channel_username, message)

        # Foydalanuvchiga tasdiq yuborish
        await event.respond("Raxmat! Ma'lumotlaringiz muvaffaqiyatli saqlandi.")

        # get_phone funksiyasini o'chiradi
        client.remove_event_handler(get_phone, events.NewMessage(from_users=event.sender_id))
    else:
        await event.respond("Iltimos, telefon raqamingizni kiriting (+998...):")

# Botni ishga tushirish
print("Bot ishga tushdi...")
client.run_until_disconnected()