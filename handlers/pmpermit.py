from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Merhaba 😎,, nasılsın şidmi şöyleki bu Userbir bot sohbeti.\n\n⚠️Rules:\n- Sohbet etmek yasak bilgileri Okuyunuz\n-Mesaj yazma spam sayılır \n\n 👉 **MÜZİK BOTUNU GRUPLARINIZA ALMAK İÇİN /KATİL KOMUTUNA BASINIZ İLK YAPMANIZ GEREKEN BOTU GRUBUNUZA EKLEMEK** @TurkishVoicebot** Denemeye değer 🤔**\n\n**Bilgileri okudunuz. KİŞİSEL BİLGİLERİ PAYLAŞMAYINIZ**\n\n**🤖 Developed by @EfsaneStar**")
  return                        
