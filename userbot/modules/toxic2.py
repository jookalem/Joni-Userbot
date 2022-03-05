from time import sleep

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.ngentot(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**WOYY ANAK NGENTOD**")
    sleep(1)
    await typew.edit("**JANGAN SOK JAGOAN DAH LU NGENTOD**")
    sleep(1)
    await typew.edit("**MUKA MASIH KAYA KONTOL AJA BELAGU NGENTOD**")
    sleep(1)
    await typew.edit("**BANGGA LU NGENTOD**")
    sleep(1)
    await typew.edit("**COBA DEH NGACA MUKA LU KAN HINA BANGET NGENTOD**")
    sleep(1)
    await typew.edit("**HAHA GOBLOK BOCAH HINA DEKIL NGENTOD**")
    sleep(1)
    await typew.edit("**TANGAN ITEM UDAH KEK TAPE ULI KONTOL**")
    sleep(1)
    await typew.edit("**DAKI DIMANA MANA UDAH KEK ORANG GAPERNAH MANDI NGENTOD**")
    sleep(1)
    await typew.edit("**MAKANNYA KALO GAMAU DIHINA MINIMAL MANDI GOBLOK**")
    sleep(1)
    await typew.edit("**NAJIS ANAK NGENTOD**")


# Create by myself @localheart


@register(outgoing=True, pattern="^.goblok(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**WOYY BOCAH GOBLOK**")
    sleep(1)
    await typew.edit("**KONTOL LU BENGKOK GOBLOK**")
    sleep(1)
    await typew.edit("**OTAK LU KECIL KEK UDANG GOBLOK**")
    sleep(1)
    await typew.edit("**MUKA BANYAK DAKI**")
    sleep(1)
    await typew.edit("**DASAR TUKANG JUALAN KAOS KAKI GOBLOK**")
    sleep(1)
    await typew.edit("**MUKA UDAH HINA**")
    sleep(1)
    await typew.edit("**UDAH GAPUNYA ORANG TUA**")
    sleep(1)
    await typew.edit("**MASIH AJA BANYAK GAYA**")
    sleep(1)
    await typew.edit("**MUKA KEK SILUMAN KERA**")
    sleep(1)
    await typew.edit("**GAUSAH BANYAK TINGKAH LO GOBLOK**")


# Create by myself @localheart


@register(outgoing=True, pattern="^.ngatain(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**EHH ANAK ANJING BEDEBAH**")
    sleep(1)
    await typew.edit("**MUKA LU KAYA LUTUNG KASARUNG**")
    sleep(1)
    await typew.edit("**SERING MAKE SARUNG**")
    sleep(1)
    await typew.edit("**EHH DASAR BOCAH SAGAPUNG**")
    sleep(1)
    await typew.edit("**GAUSAH BANYAK GAYA LO BOCAH KAMPUNG**")
    sleep(1)
    await typew.edit("**MUKA KEK PEMULUNG**")
    sleep(1)
    await typew.edit("**JANGAN SO KEREN LU LUTUNG**")
    sleep(1)
    await typew.edit("**KONTOL LU AJA MASIH BENGKOK**")
    sleep(1)
    await typew.edit("**GAUSAH BANYAK GAYA LU SILUMAN AYAM BANGKOK**")
    sleep(1)
    await typew.edit("**NANTI PALALO GUA GETOK**")


# Create by myself @localheart

CMD_HELP.update(
    {
        "toxic2": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ngentot`\
    \n↳ : Lu Coba Sendiri Aja."
        "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.goblok`\
    \n↳ : Lu Coba Sendiri Aja."
        "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ngatain`\
    \n↳ : Lu Coba Sendiri Aja."
    }
)
