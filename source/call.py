from pyrogram import Client, filters

@Client.on_message(filters.video_chat_started)
async def brah(client: Client, message):
    await message.reply("**المكالمه تقفلت ↞ أصواتكم كانت تفتح النفس 🍧🙊**")

@Client.on_message(filters.video_chat_ended)
async def bra(client: Client, message):
    await message.reply(".↞ فتحوا المكالمه اللي وده يسمعنا صوته يصعد 🦦.**")

@Client.on_message(filters.video_chat_members_invited)
async def fuckoff(client: Client, message):
    text = f"قام : {message.from_user.mention}.\n"
    x = 0
    for user in message.video_chat_members_invited.users:
        try:
            text += f"بدعوة -> {user.mention}.\nإلي المحادثة المرئية."
            x += 1
        except Exception:
            pass
    try:
        await message.reply(f"**{text}**", reply_to_message_id=message.message_id)
    except:
        pass
