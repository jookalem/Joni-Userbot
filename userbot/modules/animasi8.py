# @greyyvbss 

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, joo_cmd


@joo_cmd(pattern="sponge(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "┈┈╱▔▔▔▔▔▔▔▔▔▔▔▏\n"
        "┈╱╭▏╮╭┻┻╮╭┻┻╮╭▏ \n"
        "▕╮╰▏╯┃╭╮┃┃╭╮┃╰▏ \n"
        "▕╯┈▏┈┗┻┻┛┗┻┻┻╮▏ \n"
        "▕╭╮▏╮┈┈┈┈┏━━━╯▏\n"
        "▕╰╯▏╯╰┳┳┳┳┳┳╯╭▏ \n"
        "▕┈╭▏╭╮┃┗┛┗┛┃┈╰▏ \n"
        "▕┈╰▏╰╯╰━━━━╯┈┈▏ν2.ο\n"
        "           **BOBBB**      ")


@joo_cmd(pattern="ngok(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "┈┏━╮╭━┓┈╭━━━━╮\n"
        "┈┃┏┗┛┓┃╭┫NGOKKKK┃\n"
        "┈╰┓▋▋┏╯╯╰━━━━╯\n"
        "╭━┻╮╲┗━━━━╮╭╮┈\n"
        "┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
        "╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
        "┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
        "┈┈┈┈┗┻┛┗┻┛┈┈┈┈")


@joo_cmd(pattern="musang(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        " ╱▏┈┈┈┈┈┈▕╲▕╲┈┈┈\n"
        "▏▏┈┈┈┈┈┈▕▏▔▔╲┈┈\n"
        "▏╲┈┈┈┈┈┈╱┈▔┈▔╲┈\n"
        "╲▏▔▔▔▔▔▔╯╯╰┳━━▀\n"
        "┈▏╯╯╯╯╯╯╯╯╱┃┈┈┈\n"
        "┈┃┏┳┳━━━┫┣┳┃┈┈┈\n"
        "┈┃┃┃┃┈┈┈┃┃┃┃┈┈┈\n"
        "┈┗┛┗┛┈┈┈┗┛┗┛┈┈┈")

    
@joo_cmd(pattern="gajah(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "┈┈┈┈╱▔▔▔▔▔╲┈╱▔╲\n"
        "┈┈┈┈▏┈┈▏╭╮▕┈▏╳▕\n"
        "┈┈┈┈▏┈┈▏┈┈▕┈╲▂╱\n"
        "┈╱▔▔╲▂╱╲▂▂┈╲▂▏▏\n"
        "╭▏┈┈┈┈┈┈┈▏╲▂▂╱┈\n"
        "┃▏┈┈┈┈▏┈┈▏┈┈┈┈┈\n"
        "╯▏┈╲╱▔╲▅▅▏┈┈┈┈\n"
        "┈╲▅▅▏▕▔▔▔▔▏┈┈┈┈")

    
@joo_cmd(pattern="liat(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,    
        "┈┈┈╭━━━━━╮┈┈┈┈┈\n"
        "┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈\n"
        "┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n"
        "┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n"
        "┈┈╭┻┊┊╰━┻━╮┈┈┈┈\n"
        "┈┈╰┳┊╭━━━┳╯┈┈┈┈\n"
        "┈┈┈┃┊┃╰━━┫┈Liatin Aja\n"
        "┈┈┈┈┈┈┏━┓┈┈┈┈┈┈")


CMD_HELP.update(
    {
    "animasi8": f"➢ **Plugin : **`animasi8`\
    \n\n ┌✪ **Command :** `{cmd}sponge`\
    \n └✪ **Function : **Mengirim Gambar SpongeBoob.\
    \n\n ┌✪ **Command :** `{cmd}ngok`\
    \n └✪ **Function : **Mengirim Gambar Babi.\
    \n\n ┌✪ **Command :** `{cmd}musang`\
    \n └✪ **Function : **Mengirim Gambar Musang.\
    \n\n ┌✪ **Command :** `{cmd}gajah`\
    \n └✪ **Function : **Mengirim Gambar Gajah.\
    \n\n ┌✪ **Command :** `{cmd}liat`\
    \n └✪ **Function : **Mengirim Gambar see."   
})
