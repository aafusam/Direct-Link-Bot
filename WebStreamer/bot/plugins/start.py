import urllib.parse
from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

db = Database(Var.DATABASE_URL, Var.SESSION_NAME)

START_TEXT = """
<i>Hello There,</i>{}\n
<i>A Telegram Bot To Generate Direct Download Link For Any Telegram File, Video, Image Or Anything Else!</i>\n
<i>Clickk On Help Button Get Get Info!</i>\n
<i><u>ðªðð¥ð¡ðð¡ð </u></i>
<b>ð Porn Content May Lead You To A Permanent Ban</b>\n\n
<i><b>Developer:</b>@YOUR_DADDY_BRO</i>"""

HELP_TEXT = """
<i>- Forward Any Telegram File Or Media.</i>
<i>- The Direct Link Will Be Generated ASAP!.</i>
<i>- You Can Add Me To Your Group/Channel For Instant Links</i>
<i>- This Is A Permanent Link</i>\n
<u> ðªðð¥ð¡ðð¡ð </u>\n
<b>ð Porn Content May Lead You To A Permanent Ban</b>\n
<i>Contact Developer Or Report Bugs</i> <b>: <a href='https://t.me/your_daddy_bro'>[ Click Here]</a></b>"""

ABOUT_TEXT = """
<b>ð§ð»MÊ É´á´á´á´ : Direct-Link-Robot</b>\n
<b>ð¹Sá´á´Êá´á´ Code : <a href='https://github.com/aafusam/Direct-Link-Bot'>Github</a></b>\n
<b>ð¹Dá´á´ á´Êá´á´á´Ê : <a href='https://telegram.me/AafuSam013'>AafuSam</a></b>\n
<b>ð¸Follow On Instagram : <a href='https://instagram.com/afiq_sam_/'>Instagram</a></b>"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Há´Êá´', callback_data='help'),
        InlineKeyboardButton('AÊá´á´á´', callback_data='about'),
        InlineKeyboardButton('CÊá´sá´', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Há´á´á´', callback_data='home'),
        InlineKeyboardButton('AÊá´á´á´', callback_data='about'),
        InlineKeyboardButton('CÊá´sá´', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Há´á´á´', callback_data='home'),
        InlineKeyboardButton('Há´Êá´', callback_data='help'),
        InlineKeyboardButton('CÊá´sá´', callback_data='close')
        ]]
    )

@StreamBot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()

def get_media_file_size(m):
    media = m.video or m.audio or m.document
    if media and media.file_size:
        return media.file_size
    else:
        return None


def get_media_file_name(m):
    media = m.video or m.document or m.audio
    if media and media.file_name:
        return urllib.parse.quote_plus(media.file_name)
    else:
        return None


@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**New Mate Joined:** \n\n__MÊ Ná´á´¡ FÊÉªá´É´á´__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sá´á´Êá´á´á´ Yá´á´Ê Bá´á´ !!__"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="__Hey, Yá´á´ á´Êá´ Bá´É´É´á´á´ á´á´ á´sá´ á´á´. Cá´É´á´á´á´á´ á´Êá´ Dá´á´ á´Êá´á´á´Ê__\n\n @AafuSam013 **TÊá´Ê WÉªÊÊ Há´Êá´ Yá´á´**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Join Our Channel To Use The Bot ð</i>",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("Já´ÉªÉ´ É´á´á´¡ ð", url=f"https://t.me/+0Oi54BOKV_A2YTI1")
                            ]]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Sá´á´á´á´ÊÉªÉ´É¢ á´¡Êá´É´É¢ á´á´É´á´á´á´á´ á´Ê á´á´á´ á´Êá´á´á´Ê</i> <b><a href='http://t.me/AafuSam013'>[ Click Here ]</a></b>",
                    parse_mode="HTML",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text=START_TEXT.format(m.from_user.mention),
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
              )                                                                         
                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**Sá´ÊÊÊ SÉªÊ, Yá´á´ á´Êá´ Bá´É´É´á´á´ á´á´ á´sá´ á´á´. Qá´Éªá´á´ÊÊ á´á´É´á´á´á´á´** @AafuSam13",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Join Our Partner Channel To Use The Bot**!\n\n**Dá´á´ á´á´ Oá´ á´ÊÊá´á´á´, OÉ´ÊÊ CÊá´É´É´á´Ê Sá´Êsá´ÊÉªÊá´Ês á´á´É´ á´sá´ á´Êá´ Bá´á´**!",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                          InlineKeyboardButton("ð¤ Join Partner Channel", url=f"https://t.me/+0Oi54BOKV_A2YTI1")],
                         [InlineKeyboardButton("ð Refresh / Try Again", url=f"https://t.me/{(await b.get_me()).username}?start=AafuSam13_{usr_cmd}")
                        
                        ]]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Sá´á´á´á´ÊÉªÉ´É¢ á´¡á´É´á´ WÊá´É´É¢. Cá´É´á´á´á´á´ á´á´** [AafuSam](https://t.me/AafuSam13).",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))
        file_name = get_media_file_name(get_msg)
        file_size = humanbytes(get_media_file_size(get_msg))

        stream_link = "https://{}/{}/{}".format(Var.FQDN, get_msg.message_id, file_name) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.message_id,
                                     file_name)

        msg_text ="""
<i><u>Hurrey! Your Link Generated !</u></i>\n
<b>ð FÉªÊá´ É´á´á´á´ :</b> <i>{}</i>\n
<b>ð¦ FÉªÊá´ ê±Éªá´¢á´ :</b> <i>{}</i>\n
<b>ð¥ Dá´á´¡É´Êá´á´á´ :</b> <i>{}</i>\n
<b>ð¸ Ná´á´á´ : LÉªÉ´á´ á´xá´ÉªÊá´á´ ÉªÉ´ 24 Êá´á´Êê±</b>\n
<i>ð Developer:</i> <b>@AafuSam13</b>
"""

        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Dá´á´¡É´Êá´á´á´ É´á´á´¡ ð¥", url=stream_link)]])
        )



@StreamBot.on_message(filters.private & filters.command(["about"]))
async def start(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Ná´á´¡ Usá´Ê Já´ÉªÉ´á´á´ **\n\n__MÊ Ná´á´¡ FÊÉªá´É´á´__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>Sá´ÊÊÊ SÉªÊ, Yá´á´ á´Êá´ Bá´É´É´á´á´ á´á´ á´sá´ á´á´. Cá´É´á´á´á´á´ á´Êá´ Dá´á´ á´Êá´á´á´Ê</i>",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Join Our Partner Channel To Use The Bot**\n\n__Dá´á´ á´á´ Oá´ á´ÊÊá´á´á´, OÉ´ÊÊ CÊá´É´É´á´Ê Sá´Êsá´ÊÉªÊá´Ês á´á´É´ á´sá´ á´Êá´ Bá´á´!__",
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton("ð¤ Join Partner Channel", url=f"https://t.me/+0Oi54BOKV_A2YTI1")
                        ]]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Sá´á´á´á´ÊÉªÉ´É¢ á´¡á´É´á´ WÊá´É´É¢. Cá´É´á´á´á´á´ á´á´__ [AafuSam](https://t.me/AafuSam13).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text=HELP_TEXT,
        parse_mode="HTML",
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
        )

