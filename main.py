from telethon import TelegramClient, events



client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

questions = [
    "👤Ismigiz (To'liq...):",
    # "💰Narxi $:",
    "📞Tel (ishlab turgani...):",
    "📍Shaxar(Qayerdan Qayerga.):"
]
user_data = {}

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    user_id = event.sender_id
    user_data[user_id] = {"answers": [], "current_question": 0}
    await client.send_message(user_id,"Asslomu alaykum! Xush kelibsiz qaysi tuman yoki shaxarga bormoqchisiz...😊")
    await client.send_message(user_id, questions[0])   

@client.on(events.NewMessage)
async def handle_message(event):
    user_id = event.sender_id

    if user_id not in user_data:
        await client.send_message(user_id, "Iltimos, /start buyrug'ini bosing.")
        return

    data = user_data[user_id]
    current_question = data["current_question"]
    
    if event.text.startswith('/start'):
        return
    if current_question < len(questions):
        data["answers"].append(event.text)

    if current_question + 1 < len(questions):
        data["current_question"] += 1
        await client.send_message(user_id, questions[current_question + 1])
    else:
        answers = data["answers"]
        message = (
            f"👤Ismi: {answers[0]}\n"
            # f"💰Narxi $: {answers[1]}\n"
            f"📞Tel: {answers[1]}\n"
            f"📍Shaxar: {answers[2]}"
        )
        # entity = await client.get_entity('https://t.me/+pFWbjP17QxllYmQy')
        # print(entity,'-----------')
        await client.send_message(group_name_or_id, message)
        await event.reply("Ma'lumotlar uchun rahmat! Xaydovchilar siz bilan bog'nishyapti... ✅")
        del user_data[user_id] 

print("Bot ishga tushdi!")
client.run_until_disconnected()