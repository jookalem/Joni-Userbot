from platform import uname

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^D(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BACOT NGENTOTTT BAPA LU SURUH RIBUT SAMA GUA**")


@register(outgoing=True, pattern="^E(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAK USAH SOK KERAS LO DONGO**")


@register(outgoing=True, pattern="^F(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MUKA LU SEMUA KAYA KONTOL**")


@register(outgoing=True, pattern="^I(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MUKA LU KEK MONYET BEKANTAN**")


@register(outgoing=True, pattern="^Q(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MUKA LU ITEM DEKIL KEK BOCAH KERDIL**")


@register(outgoing=True, pattern="^R(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BACOT NIH BOCAH KAMPUNG**")


@register(outgoing=True, pattern="^T(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BERISIK NGENTODDD**")


@register(outgoing=True, pattern="^U(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MUKA LU KEK SILUMAN BABI**")


@register(outgoing=True, pattern="^W(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BAPA LU KAKINYA BUNTUNG GOBLOK**")


@register(outgoing=True, pattern="^Q(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BACOTAN LU GAK BIKIN GUA KETAR KETIR TOLOL**")


CMD_HELP.update(
    {
        "toxic": "D\
\nUsage: Coba Aja Bruh.\
\n\nE\
\nUsage: Coba Aja Bruh.\
\n\nF\
\nUsage: Coba Aja Bruh.\
\n\nI\
\nUsage: Coba Aja Bruh.\
\n\nQ\
\nUsage: Coba Aja Bruh.\
\n\nR\
\nUsage: Coba Aja Bruh.\
\n\nT\
\nUsage: Coba Aja Bruh.\
\n\nU\
\nUsage: Coba Aja Bruh.\
\n\nW\
\nUsage: Coba Aja Bruh.\
\n\nQ\
\nUsage: Coba Aja Bruh."
    }
)
