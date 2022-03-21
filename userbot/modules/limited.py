from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.utils import joo_cmd


@joo_cmd(pattern="limit(?: |$)(.*)")
async def _(event):
    await event.edit("`Bentar Lagi Gua Cek Anjing`")
    async with bot.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("`Boss! Please Unblock @SpamBot`")
            return
        await event.edit(f"~ {response.message.message}")


CMD_HELP.update({"limit": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}limit`" "\n•: Untuk Mengecek Limit Akun"})
