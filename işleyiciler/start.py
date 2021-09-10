from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Merhabalar 👋{message.from_user.first_name}!
\nTelegram'ın sesli sohbetinde müzik dinlemek için yazılmış açık kaynak kodlu müzik ve video izleme botudur.
\n\nGruplarınıza alıp müzik dinleme ve video izleme keyfini çıkarın, Müzik ve ücretsiz olduğu için ufak problemler olabilir. 
\nBotun komutları için /help komutuna basınız.
\n\nDeveloped Sahip 🇹🇷 [ADSIZ KAPTAN](https://t.me/Kizilsancaksahibi) 
  </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎵 Music Kanalım", url="https://t.me/Solofej",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/Smailesi"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 Yardımcı Sahip", url="https://t.me/TeleWistKral"
                    ),
                    InlineKeyboardButton(
                        "🇹🇷 TR dil desteği", url="https://t.me/KanliReis"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Grubunuza Ekle ➕", url="https://t.me/Ellycarlmusicbot?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️YouTube videosu aramak istiyor musunuz? ?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/Smailesi"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n/oynat <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/oynatlist - Show now playing list
/bilgi - Show now playing
/bul <song name> - download songs you want quickly
/link <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/klip <song name> - download videos you want quickly
\n*Admins only*
/liste - open music player settings panel
/durdur - pause song play
/devam - resume song play
/atla - play next song
/bitir- stop music play
/katil - invite assistant to your chat
/ayril - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎵 müzik kanal", url="https://t.me/Smailesi"
                    )
                ]
            ]
        )
    )    
