# 🍀 © @tofik_dn
# ⚠️ Do not remove credits

import requests

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import skyzu_cmd


@skyzu_cmd(pattern="asupan$")
async def _(event):
    try:
        response = requests.get("https://api-tede.herokuapp.com/api/asupan/ptl").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan Video Asupan.**")


@skyzu_cmd(pattern="wibu$")
async def _(event):
    try:
        response = requests.get("https://api-tede.herokuapp.com/api/asupan/wibu").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan Video Wibu.**")


@skyzu_cmd(pattern="chika$")
async def _(event):
    try:
        response = requests.get("https://api-tede.herokuapp.com/api/chika").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan Video Chikakiku.**")


@skyzu_cmd(pattern="bocil$")
async def _(event):
    try:
        response = requests.get(
            "https://api-alphabot.herokuapp.com/api/asupan/bocil?apikey=Alphabot"
        ).json()
        await event.client.send_file(event.chat_id, response["result"])
        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan video asupan bocil.**")


CMD_HELP.update(
    {
        "asupan": f"**Plugin : **`asupan`\
        \n\n  •  **Syntax :** `{cmd}asupan`\
        \n  •  **Function : **Untuk Mengirim Video Asupan secara random.\
        \n\n  •  **Syntax :** `{cmd}wibu`\
        \n  •  **Function : **Untuk Mengirim Video Wibu secara random.\
        \n\n  •  **Syntax :** `{cmd}chika`\
        \n  •  **Function : **Untuk Mengirim Video Chikakiku secara random.\
        \n\n  •  **Syntax :** `{cmd}bocil`\
        \n  •  **Function : **Untuk Mengirim Video Bocil secara random.\
    "
    }
)
