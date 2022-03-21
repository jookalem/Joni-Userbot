""" Userbot module for other small commands. """
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import joo_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@joo_cmd(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**✨Halo {DEFAULTUSER} Jika Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/ikhsanntarjo)"
        "\n[Github](https://github.com/jookalen/Joni-Userbot)"
    )


@joo_cmd(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/Skyzu/skyzu-userbot/skyzu-userbot/varshelper.txt)"
    )


CMD_HELP.update(
    {
        "helper": "`.lhelp`\
\nUsage: Bantuan Untuk Joni-Userbot.\
\n`.vars`\
\nUsage: Melihat Daftar Vars."
    }
)
