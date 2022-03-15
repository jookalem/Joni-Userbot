from platform import uname
from time import sleep

from userbot import ALIVE_NAME
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, WEATHER_DEFCITY
from userbot.utils import skyzu_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@skyzu_cmd(pattern="g(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("**GA NYAMBUNG GOBLOK**")


# Pantun


@skyzu_cmd(pattern="p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Salam Dulu Biar Sopan...`")


# Salam


@skyzu_cmd(pattern="l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Waalaikumsalam brodie...`")


# Menjawab Salam


@skyzu_cmd(pattern="kenalin(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("☑️ `Skyzu Kuli Jawa`")
    sleep(2)
    await typew.edit("✅ `Skyzu Kuli Jawa`")
    sleep(1)
    await typew.edit("☑️ `Dior Stres`")
    sleep(2)
    await typew.edit("✅ `Dior Stres`")
    sleep(1)
    await typew.edit("☑️ `Kyura Sakit Jiwa`")
    sleep(2)
    await typew.edit("✅ `Kyura Sakit Jiwa`")
    sleep(1)
    await typew.edit("☑️ `Kyy Sering Coli`")
    sleep(2)
    await typew.edit("✅ `Kyy Sering Coli`")
    sleep(1)
    await typew.edit("☑️ `Kitaro Autis`")
    sleep(2)
    await typew.edit("✅ `Kitaro Autis`")
    sleep(1)
    await typew.edit(
        "`⚡ Cuma Joni Yang Paling Waras, Baik Hati, Ganteng, Calon Imam Mu 🤪`"
    )


# King Userbot Support


@skyzu_cmd(pattern="istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Heh Kamu Gaboleh Begitu...`")
    sleep(2)
    await event.edit("`اَسْتَغْفِرُاللهَ الْعَظِيْم`")


# Istigfar


@skyzu_cmd(pattern="virtual(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**OOOO**")
    sleep(1.5)
    await typew.edit("**INI YANG VIRTUAL**")
    sleep(1.5)
    await typew.edit("**YANG KATANYA SAYANG BANGET**")
    sleep(1.5)
    await typew.edit("**TAPI TETEP AJA DI TINGGAL**")
    sleep(1.5)
    await typew.edit("**NI INGET**")
    sleep(1.5)
    await typew.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    sleep(1.5)
    await typew.edit("**APALAGI OMONGANNYA**")
    sleep(1.5)
    await typew.edit("**BHAHAHAHA**")
    sleep(1.5)
    await typew.edit("**KASIAN MANA MASIH MUDA**")


@skyzu_cmd(pattern="perkenalkan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai Guys , Perkenalkan Nama Gw {DEFAULTUSER}`")
    sleep(2)
    await event.edit(f"`Gw Tinggal Di {WEATHER_DEFCITY}`")
    sleep(2)
    await event.edit("`Salam Kenal...`")
    sleep(2)
    await event.edit("`Udah Gitu Aja :v`")


# Perkenalan


@skyzu_cmd(pattern="joni(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Hi guys..**")
    sleep(1)
    await typew.edit("**Kembali lagi bersama gua Joni ygy..**")
    sleep(1)
    await typew.edit("**Anjay srepett..**")
    sleep(1)
    await typew.edit("**Cuman Joni Paling Ganteng Setelegram..**")
    sleep(1)
    await typew.edit("**A EN JE A YE**")
    sleep(1)
    await typew.edit("**AAANNNJJJAAAYYY**")
    sleep(1)
    await typew.edit("**SREPETTT**")
    sleep(1)
    await typew.edit("**Joni Joni Yes Papa**")
    sleep(1)
    await typew.edit("**Lu Belum Keren Kalo Belum Pake Repo Joni**")
    sleep(1)
    await typew.edit("**Tapi Bo'ong Hayuukk papale papale**")


# Create by myself @ikhsanntarjo


CMD_HELP.update(
    {
        "gabut": f"**Modules** - `Gabut`\
        \n\n Cmd : `{cmd}l`\
        \nUsage : Untuk Menjawab Salam\
        \n\n Cmd : `{cmd}perkenalkan`\
        \nUsage : Memperkenalkan Diri\
        \n\n Cmd : `{cmd}virtual`\
        \nUsage : ngeledek orang yang virtual\
        \n\n Cmd : `{cmd}g`\
        \nUsage : Member Goblok\
        \n\n Cmd : `{cmd}kenalin`\
        \nUsage : Awokwok\
        \n\n Cmd : `{cmd}joni`\
        \nUsage : perkenalan Joni\
        \n\n Cmd : `{cmd}p`\
        \nUsage : Untuk Memberi Salam\
    "
    }
)
