import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import ALIVE_NAME
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import joo_cmd


@joo_cmd(pattern="slogo(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Give a name too!`")
    else:
        await event.edit("`Processing...`")
    chat = "@GreyCilik_bot"
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(f"/logo {text}")
            response = await conv.get_response()
            logo = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @GreyCilik_bot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            logo,
            caption=f"Logo by [{ALIVE_NAME}](tg://user?id={aing.id})",
        )
        await event.client.delete_messages(conv.chat_id, [msg.id, response.id, logo.id])
        await event.delete()


CMD_HELP.update(
    {
        "slogo": f"**Plugin : **`slogo`\
        \n\n  •  **Syntax :** `{cmd}slogo` <text>\
        \n  •  **Function : **Untuk Membuat Logo Pale FOTO Cewek\
    "
    }
)
