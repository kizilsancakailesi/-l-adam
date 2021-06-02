from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Halo,, ini adalah assistent service dari @zeldamusicbot .\n\n⚠️Rules:\n- Dilarang Chat Disini\n-Dilarang Spam Disini \n\n 👉 **KIRIM TAUTAN GROUP ANDA KESINI ATAU UNDANG** @zeldamusicbot **KE GROUP ANDA**\n\n**JANGAN LUPA JOIN** @Friendlycircle\n\n**🤖 Developed by @oppaidasukii**")
  return                        
