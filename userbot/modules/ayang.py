# @greyyvbss


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import skyzu_cmd
import random
from userbot import owner
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos


@skyzu_cmd(pattern="ayang$")
async def _(event):
    try:
        ayangnya = [
            ayang
            async for ayang in event.client.iter_messages(
                "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ayangnya),
            caption=f"Nih Ayang Aku 😘 [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Gada Yang Mau Sama Kamu Karena Kamu ga Gud Luking🤪.")


CMD_HELP.update(
    {
        "ayang": f"**Plugin : **ayang\
        \n\n  •  **Syntax :** {cmd}ayang\
        \n  •  **Function : **Untuk Mencari Ayang Buat Cowo Yang Jomblo.\
    "
    }
)
