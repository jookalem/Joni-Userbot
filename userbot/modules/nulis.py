# from ultroid
# © @greyyvbss
# ⚠️ Don't Remove Credits
# recode by @ikhsanntarjo

import os

from PIL import Image, ImageDraw, ImageFont
from userbot.utils import joo_cmd, edit_or_reply, edit_delete, text_set
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP

@joo_cmd(pattern="nulis1(?: |$)(.*)")
async def writer(event):
    if event.reply_to:
        reply = await event.get_reply_message()
        text = reply.message
    elif event.pattern_match.group(1).strip():
        text = event.text.split(maxsplit=1)[1]
    else:
        return await edit_delete(event, "Berikan Beberapa Teks Untuk Di Tulis")
    k = await edit_or_reply(event, "Sedang Memproses, Mohon Tunggu...")
    img = Image.open("resources/kertas.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("resources/assfont.ttf", 30)
    x, y = 150, 140
    lines = text_set(text)
    line_height = font.getsize("hg")[1]
    for line in lines:
        draw.text((x, y), line, fill=(1, 22, 55), font=font)
        y = y + line_height - 5
    file = "cilik.jpg"
    img.save(file)
    await event.reply(file=file)
    os.remove(file)
    await k.delete()


@joo_cmd(pattern="nulis2(?: |$)(.*)")
async def writer(event):
    if event.reply_to:
        reply = await event.get_reply_message()
        text = reply.message
    elif event.pattern_match.group(1).strip():
        text = event.text.split(maxsplit=1)[1]
    else:
        return await edit_delete(event, "Berikan Beberapa Teks Untuk Di Tulis")
    k = await edit_or_reply(event, "Sedang Memproses, Mohon Tunggu...")
    img = Image.open("resources/buku.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("resources/assfont.ttf", 30)
    x, y = 150, 140
    lines = text_set(text)
    line_height = font.getsize("hg")[1]
    for line in lines:
        draw.text((x, y), line, fill=(1, 22, 55), font=font)
        y = y + line_height - 5
    file = "grey.jpg"
    img.save(file)
    await event.reply(file=file)
    os.remove(file)
    await k.delete()


CMD_HELP.update(
    {
        "nulis": f"**plugin : **`nulis`\ 
        \n\n  •  **syntax :** `{cmd}nulis1` <text>\
        \n  •  **function : **Menulis Teks Di Buku ,Buat Lu Yang Mager Nulis\
        \n\n  •  **syntax :** `{cmd}nulis2` <text>\
        \n  •  **function : **Menulis Teks Di Buku ,Buat Lu Yang Mager Nulis\
    "
    }
)
