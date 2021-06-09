# Nasıl mı yüklenir 🤔
Bu Botu dağıtmanın en kolay yolu 
<p align="center"><a href="https://heroku.com/deploy?template=https://github.com/Mehmetbaba06/Muzik_Asistan_Telegram"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-red?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p>

Get STRING_NAME from here:

[![GenerateString](https://img.shields.io/badge/repl.it-generateString-yellowgreen)](https://replit.com/@QueenArzoo/VCPlayBot)

### Mandatory Vars.

- Some Of The Mandatory Vars Are :-
   - `API_ID` :  Give API_ID of your Alternate Telegram Account. also get from here [@APIInfoBot](https://t.me/APIinfoBot)
   - `API_HASH` :  Give API_HASH of your Alternate Telegram Account. also get from here [@APIInfoBot](https://t.me/APIinfoBot)
   - `BOT_TOKEN` :  Make a Bot from [@Botfather](https://t.me/botfather) and fill it's bot token.
## Commands 🛠

- '/oynat <song name>' - istediğiniz şarkıyı çalın
- '/dplay <song adı>' - deezer aracılığıyla istediğiniz şarkıyı çalın
- '/splay <song name>' - jio saavn aracılığıyla istediğiniz şarkıyı çalın
- '/oynatlist' - Şimdi çalma listesini göster
- '/geçerli' - Şimdi oynatıyor göster
- '/yükle <song name>' - istediğiniz şarkıları hızlı bir şekilde indirin
- '/link <query>' - youtube'da detayları içeren videoları arayın
- '/deezer <song adı>' - deezer aracılığıyla istediğiniz şarkıları hızlı bir şekilde indirin
- '/saavn <song adı>' - istediğiniz şarkıları saavn üzerinden hızlı bir şekilde indirin
- '/video indirme komutu kısaca. 
#### Admins only.
- '/oyuncu' - müzik çalar ayarları panelini açma
- '/durdur' - şarkı çalmayı duraklat
- '/devam' - şarkı çalmaya devam et
- '/atla' - sonraki şarkıyı çal
- '/bitir' - müzik çalmayı durdur
- '/katil' - asistanı sohbetinize davet edin
- '/ayril' - asistanı sohbetinizden çıkarın
- '/admincache' - Yönetici listesini yenile

## Requirements

- FFmpeg
- Python 3.7+

## Deployment

### Config

Copy `example.env` to `.env` and fill it with your credentials.

### The good way

1. Install Python requirements:
   ```bash
   pip install -U -r requirements.txt
   ```
2. Run:
   ```bash
   python main.py
   ```

### Docker

1. Build:
   ```bash
   docker build -t musicplayer .
   ```
2. Run:
   ```bash
   docker run --env-file .env musicplayer
   ```

## License

### GNU Affero General Public License v3.0

[Read more](http://www.gnu.org/licenses/#AGPL)
