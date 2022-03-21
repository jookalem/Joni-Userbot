from platform import uname

from userbot import ALIVE_NAME
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.events import register
from userbot.utils import joo_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^P(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Assalamu'alaikum...**")


@skyzu_cmd(pattern="atg(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Astaghfirullah...**")


@register(outgoing=True, pattern="^L(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Wa'alaikumsalam...**")


@skyzu_cmd(pattern="dor(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**DAR DER DOR MENTAL BAPAK LU GUA GEDOR**"
    )


@register(outgoing=True, pattern="^K(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KONTOL LU NANAHAN BEGO**")


@register(outgoing=True, pattern="^N(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**UDAH MISKIN HIDUP LAGI NAJIS**")


@register(outgoing=True, pattern="^B(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BACOT NIH YATIM PIATU**")


@register(outgoing=True, pattern="^M(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MASIH KECIL MENDING TIDUR**")


@register(outgoing=True, pattern="^Y(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**MAKAN ULAT SAGU DIPINGGIR JALAN TOL, LO GAUSAH BELAGU KONTOL**"
    )


@register(outgoing=True, pattern="^C(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**DIEM BEGO, MULUT LU BAU CIU**")


@register(outgoing=True, pattern="^S(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BACOT NIH SILUMAN KERA**")


@register(outgoing=True, pattern="^V(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAADA BAGUS BAGUSNYA LO BEGITU TOLOL**")


@register(outgoing=True, pattern="^J(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MUKA LU KEK GEMBELAN PASAR**")


@register(outgoing=True, pattern="^A(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**DIEM LU ANAK ANJING**")


@register(outgoing=True, pattern="^X(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAUSAH SO KEREN BEGO**")


@register(outgoing=True, pattern="^Z(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**Si Paling Anak War**"
    )


@register(outgoing=True, pattern="^H(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**EMAK LU NOH LAGI NGELACUR**")


@register(outgoing=True, pattern="^O(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GUA SI CUEK**")


@register(outgoing=True, pattern="^G(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BERISIK BEGO BOCAH KAMPUNG**")


CMD_HELP.update(
    {
        "salam": "P\
\nUsage: Untuk Memberi salam.\
\n\nL\
\nUsage: Untuk Menjawab Salam.\
\n\nK\
\nUsage: Coba Aja Bruh.\
\n\nN\
\nUsage: Coba Aja Bruh.\
\n\nB\
\nUsage: Coba Aja Bruh.\
\n\nM\
\nUsage: Coba Aja Bruh.\
\n\nY\
\nUsage: Coba Aja Bruh.\
\n\nC\
\nUsage: Coba Aja Bruh.\
\n\nS\
\nUsage: Coba Aja Bruh."
    }
)

CMD_HELP.update(
    {
        "salam2": f"V\
\nUsage: Coba Aja Bruh.\
\n\nJ\
\nUsage: Coba Aja Bruh.\
\n\nA\
\nUsage: Coba Aja Bruh.\
\n\nX\
\nUsage: Coba Aja Bruh.\
\n\nZ\
\nUsage: Coba Aja Bruh.\
\n\nH\
\nUsage: Coba Aja Bruh.\
\n\n{cmd}atg\
\nUsage: Istighfar.\
\n\n{cmd}dor\
\nUsage: Coba Aja Bruh.\
\n\nO\
\nUsage: Coba Aja Bruh.\
\n\nG\
\nUsage: Coba Aja Bruh."
    }
)
