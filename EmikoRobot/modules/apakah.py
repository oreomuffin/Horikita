import random
from EmikoRobot.events import register
from EmikoRobot import telethn

APAKAH_STRING = ["Iyaa sayang", 
                 "Tidak", 
                 "Mungkin", 
                 "Mana saya tau", 
                 "Bisa jadi", 
                 "Mungkin Tidak",
                 "Iyaa",
                 "Iyain aja dah biar cepet",
                 "Jangan tanya saya, saya kan bot",
                 "Apa, ulang?",
                 "Gatau mau jawab apa"
                 ]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan saya pertanyaan 😐')
        return
    await event.reply(random.choice(APAKAH_STRING))
