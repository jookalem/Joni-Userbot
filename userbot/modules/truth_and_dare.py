# Ported by Fariz (Flicks-Userbot)

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP, bot
from userbot.utils import joo_cmd


@joo_cmd(pattern="truth(?: |$)(.*)")
async def _(event):
    await event.edit("Mengirim pesan truth...")
    async with bot.conversation("@truthordares_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1335899453)
            )
            await conv.send_message("/truth")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("Harap unblock `@truthordares_bot` dan coba lagi")
            return
        await event.edit(f"**#TRUTH**\n\n{response.message.message}")


@joo_cmd(pattern="dare(?: |$)(.*)")
async def _(event):
    await event.edit("Mengirim pesan dare...")
    async with bot.conversation("@truthordares_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1335899453)
            )
            await conv.send_message("/dare")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("Harap unblock `@truthordares_bot` dan coba lagi")
            return
        await event.edit(f"**#DARE**\n\n{response.message.message}")


@joo_cmd(pattern="spill(?: |$)(.*)")
async def _(event):
    await event.edit("Mengirim pesan spill...")
    async with bot.conversation("@Spillgame_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1361222893)
            )
            await conv.send_message("/spill")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("Harap unblock `@Spillgame_bot` dan coba lagi")
            return
        await event.edit(f"**Pesan spill**\n\n{response.message.message}")


CMD_HELP.update(
    {
        "truth_dare": "** Plugin :** truth_dare\
        \n\n  •  Perintah : `{cmd}truth`\
        \n  •  Function : Untuk Mengirim Pesan Truth\
        \n\n  •  Perintah : `{cmd}dare`\
        \n  •  Function : Untuk Mengirim Pesan Dare\
        \n\n  •  Perintah : `{cmd}spill`\
        \n  •  Function : Untuk Mengirim Pesan Pertanyaan\
    "
    }
)
