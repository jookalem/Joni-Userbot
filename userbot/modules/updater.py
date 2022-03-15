"""
This module updates the userbot based on upstream revision
"""

import asyncio
import sys
from os import environ, execle, path, remove

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

from userbot import BOTLOG, BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import (
    CMD_HELP,
    HEROKU_API_KEY,
    HEROKU_APP_NAME,
    UPSTREAM_REPO_BRANCH,
    UPSTREAM_REPO_URL,
)
from userbot.utils import skyzu_cmd

requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), "requirements.txt"
)


async def gen_chlog(repo, diff):
    ch_log = ""
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff):
        ch_log += (
            f"•[{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n"
        )
    return ch_log


async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            " ".join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


async def deploy(event, repo, ups_rem, ac_br, txt):
    if HEROKU_API_KEY is not None:
        import heroku3

        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_app = None
        heroku_applications = heroku.apps()
        if HEROKU_APP_NAME is None:
            await event.edit(
                "`[HEROKU]: Harap Siapkan Variabel` **HEROKU_APP_NAME** `"
                " untuk dapat deploy perubahan terbaru dari ⚡𝐉ᴏɴɪ-𝐔sᴇʀʙᴏᴛ⚡.`"
            )
            repo.__del__()
            return
        for app in heroku_applications:
            if app.name == HEROKU_APP_NAME:
                heroku_app = app
                break
        if heroku_app is None:
            await event.edit(
                f"{txt}\n`Kredensial Heroku tidak valid untuk deploy 𝐉ᴏɴɪ-𝐔sᴇʀʙᴏᴛ dyno.`"
            )
            return repo.__del__()
        await event.edit(
            "**[HEROKU] Sedang MengUpdate**" "\nMohon Mohon Menunggu 5-7 Menit"
        )
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", "https://api:" + HEROKU_API_KEY + "@"
        )
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
            remote.push(refspec="HEAD:refs/heads/master", force=True)
        except GitCommandError as error:
            await event.edit(f"{txt}\n`Terjadi Kesalahan Di Log:\n{error}`")
            return repo.__del__()
        build = app.builds(order_by="created_at", sort="desc")[0]
        if build.status == "failed":
            await event.edit(
                "`Build Gagal!\n" "Dibatalkan atau ada beberapa kesalahan...**"
            )
            await asyncio.sleep(5)
            return await event.delete()
        else:
            await event.edit(
                "**⚡𝐉ᴏɴɪ-𝐔sᴇʀʙᴏᴛ⚡​ Berhasil DiUpdate,Restart Tunggu Sebentar Tod**"
            )
            await asyncio.sleep(15)
            await event.delete()

        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID, "#BOT \n" "**⚡𝐉ᴏɴɪ-𝐔sᴇʀʙᴏᴛ⚡ Berhasil Di Update Tod**"
            )

    else:
        await event.edit(
            "`[HEROKU]:" "\nHarap Siapkan Variabel` **HEROKU_API_KEY** `.`"
        )
        await asyncio.sleep(10)
        await event.delete()
    return


async def update(event, repo, ups_rem, ac_br):
    try:
        ups_rem.pull(ac_br)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    await update_requirements()
    await event.edit("**𝐉ᴏɴɪ-𝐔sᴇʀʙᴏᴛ​** `Berhasil Di Update!`")
    await asyncio.sleep(1)
    await event.edit("**𝐉ᴏɴɪ-𝐔sᴇʀʙᴏᴛ​** `Di Restart....`")
    await asyncio.sleep(1)
    await event.edit("`Mohon Menunggu Beberapa Detik.`")
    await asyncio.sleep(10)
    await event.delete()

    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, "#BOT \n" "**⚡𝐉ᴏɴɪ-𝐔sᴇʀʙᴏᴛ​⚡ Telah Di Perbarui Tod**"
        )
        await asyncio.sleep(100)
        await event.delete()

    # Spin a new instance of bot
    args = [sys.executable, "-m", "userbot"]
    execle(sys.executable, *args, environ)
    return


@skyzu_cmd(pattern="update(?: |$)(now|deploy)?")
@register(incoming=True, from_users=DEVS,
          pattern=r"^\.cupdate(?: |$)(now|deploy)?")
async def upstream(event):
    "For .update command, check if the bot is up to date, update if specified"
    await event.edit("**Mengecek Pembaruan, Silakan Menunggu....**")
    conf = event.pattern_match.group(1)
    off_repo = UPSTREAM_REPO_URL
    force_update = False
    try:
        txt = "`Mohon Maaf, Pembaruan Tidak Dapat Di Lanjutkan Karna "
        txt += "Beberapa Masalah Terjadi`\n\n**LOGTRACE:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await event.edit(f"{txt}\n`Directory {error} Tidak Dapat Di Temukan`")
        return repo.__del__()
    except GitCommandError as error:
        await event.edit(f"{txt}\n`Gagal Awal! {error}`")
        return repo.__del__()
    except InvalidGitRepositoryError as error:
        if conf is None:
            return await event.edit(
                f"`Sayangnya, Directory {error} Tampaknya Bukan Dari Repo."
                "\nTapi Kita Bisa Memperbarui Paksa Userbot Menggunakan .update now.`"
            )
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        force_update = True
        repo.create_head("master", origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)

    ac_br = repo.active_branch.name
    if ac_br != UPSTREAM_REPO_BRANCH:
        await event.edit(
            "**[UPDATER]:**\n"
            f"`Looks like you are using your own custom branch ({ac_br}). "
            "in that case, Updater is unable to identify "
            "which branch is to be merged. "
            "please checkout to any official branch`"
        )
        return repo.__del__()
    try:
        repo.create_remote("upstream", off_repo)
    except BaseException:
        pass

    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)

    changelog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")

    if changelog == "" and force_update is False:
        await event.edit(f"\n**⚡𝐉ᴏɴɪ-𝐔sᴇʀʙᴏᴛ⚡​ Sudah Versi Terbaru Tod**\n")
        await asyncio.sleep(15)
        await event.delete()
        return repo.__del__()

    if conf is None and force_update is False:
        changelog_str = f"**Pembaruan Untuk ⚡𝐉ᴏɴɪ-𝐔sᴇʀʙᴏᴛ​⚡ :\n\n⚒️ Pembaruan Data :**\n`{changelog}`"
        if len(changelog_str) > 4096:
            await event.edit("`Changelog Terlalu Besar, Lihat File Untuk Melihatnya.`")
            file = open("output.txt", "w+")
            file.write(changelog_str)
            file.close()
            await event.client.send_file(
                event.chat_id,
                "output.txt",
                reply_to=event.id,
            )
            remove("output.txt")
        else:
            await event.edit(changelog_str)
        return await event.respond(
            f"**Perintah Untuk Update, Sebagai Berikut.**\n 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:`{cmd}update now`\n 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:`{cmd}update deploy`\n\nUntuk Meng Update Fitur Terbaru Dari **⚡𝐉ᴏɴɪ-𝐔sᴇʀʙᴏᴛ​⚡**"
        )

    if force_update:
        await event.edit(
            "`Sinkronisasi Paksa Ke Kode Userbot Stabil Terbaru, Harap Tunggu .....`"
        )
    else:
        await event.edit("` Proses Update ⚡𝐉ᴏɴɪ-𝐔sᴇʀʙᴏᴛ​⚡ Loading....1%`")
        await event.edit("` Proses Update ⚡𝐉ᴏɴɪ-𝐔sᴇʀʙᴏᴛ⚡ Loading....20%`")
        await event.edit("` Proses Update ⚡𝐉ᴏɴɪ-𝐔sᴇʀʙᴏᴛ⚡​ Loading....35%`")
        await event.edit("` Proses Update ⚡𝐉ᴏɴɪ-𝐔sᴇʀʙᴏᴛ⚡ Loading....77%`")
        await event.edit("` Proses Update ⚡𝐉ᴏɴɪ-𝐔sᴇʀʙᴏᴛ⚡​ Updating...90%`")
        await event.edit(
            "` Proses Update ⚡𝐉ᴏɴɪ-𝐔sᴇʀʙᴏᴛ⚡​ Mohon Tunggu Sebentar....100%`"
        )

    if conf == "now":
        await update(event, repo, ups_rem, ac_br)
        await asyncio.sleep(10)
        await event.delete()
    elif conf == "deploy":
        await deploy(event, repo, ups_rem, ac_br, txt)
        await asyncio.sleep(10)
        await event.delete()
    return


CMD_HELP.update(
    {
        "update": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}update`"
        "\n• : Untuk Melihat Pembaruan Terbaru Joni-Userbot."
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}update now`"
        "\n• : Memperbarui Joni-Userbot."
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}update deploy`"
        "\n• : Memperbarui Joni-Userbot Dengan Cara Men-Deploy Ulang."
    }
)
