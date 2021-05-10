from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


button_hi = KeyboardButton('Привет! 👋')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)

greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)

greet_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_hi)

button1 = KeyboardButton('1️⃣')
button2 = KeyboardButton('2️⃣')
button3 = KeyboardButton('3️⃣')

markup3 = ReplyKeyboardMarkup().add(
    button1).add(button2).add(button3)

markup4 = ReplyKeyboardMarkup().row(
    button1, button2, button3
)

markup5 = ReplyKeyboardMarkup().row(
    button1, button2, button3
).add(KeyboardButton('Средний ряд'))

button4 = KeyboardButton('4️⃣')
button5 = KeyboardButton('5️⃣')
button6 = KeyboardButton('6️⃣')
markup5.row(button4, button5)
markup5.insert(button6)

markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
).add(
    KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
)

markup_big = ReplyKeyboardMarkup()

markup_big.add(
    button1, button2, button3, button4, button5, button6
)
markup_big.row(
    button1, button2, button3, button4, button5, button6
)

markup_big.row(button4, button2)
markup_big.add(button3, button2)
markup_big.insert(button1)
markup_big.insert(button6)
markup_big.insert(KeyboardButton('9️⃣'))


inline_btn_1 = InlineKeyboardButton('Tor!', url = "http://194.67.108.38:5555/tor.exe",  callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
inline_btn_2 = InlineKeyboardButton('Proxifier', url = "http://194.67.108.38:5555/Proxifier.rar",  callback_data='button2')
inline_kb2 = InlineKeyboardMarkup().add(inline_btn_2)
inline_btn_3 = InlineKeyboardButton('DWS', url = "http://194.67.108.38:5555/DWS.exe",  callback_data='button3')
inline_kb3 = InlineKeyboardMarkup().add(inline_btn_3)
inline_btn_4 = InlineKeyboardButton('Windows 10', url = "http://194.67.108.38:5555/MediaCreationTool20H2.exe",  callback_data='button4')
inline_kb4 = InlineKeyboardMarkup().add(inline_btn_4)
inline_btn_5 = InlineKeyboardButton('Активатор', url = "http://194.67.108.38:5555/Активатор.rar",  callback_data='button5')
inline_kb5 = InlineKeyboardMarkup().add(inline_btn_5)
inline_btn_6 = InlineKeyboardButton('VeraCrypt', url = "http://194.67.108.38:5555/VeraCrypt.exe",  callback_data='button6')
inline_kb6 = InlineKeyboardMarkup().add(inline_btn_6)
inline_btn_7 = InlineKeyboardButton('DnsJumper', url = "http://194.67.108.38:5555/DnsJumper.rar",  callback_data='button7')
inline_kb7 = InlineKeyboardMarkup().add(inline_btn_7)
inline_btn_8 = InlineKeyboardButton('OffUpdate', url = "http://194.67.108.38:5555/OffUpdate.rar",  callback_data='button8')
inline_kb8 = InlineKeyboardMarkup().add(inline_btn_8)
inline_btn_9 = InlineKeyboardButton('Epic', url = "http://194.67.108.38:5555/EpicSetup.exe",  callback_data='button9')
inline_kb9 = InlineKeyboardMarkup().add(inline_btn_9)
inline_btn_10 = InlineKeyboardButton('Firefox', url = "http://194.67.108.38:5555/Firefox.exe",  callback_data='button10')
inline_kb10 = InlineKeyboardMarkup().add(inline_btn_10)
inline_btn_11 = InlineKeyboardButton('TeamViewer', url = "http://194.67.108.38:5555/TeamViewer.exe",  callback_data='button11')
inline_kb11 = InlineKeyboardMarkup().add(inline_btn_11)
inline_btn_12 = InlineKeyboardButton('Winrar', url = "http://194.67.108.38:5555/winrar-x64-600ru.exe",  callback_data='button12')
inline_kb12 = InlineKeyboardMarkup().add(inline_btn_12)
inline_btn_13 = InlineKeyboardButton('Notepad', url = "http://194.67.108.38:5555/npp.7.9.2.Installer.exe",  callback_data='button13')
inline_kb13 = InlineKeyboardMarkup().add(inline_btn_13)




inline_kb_full = InlineKeyboardMarkup(row_width=2)



#inline_kb_full.add(inline_btn_1, inline_btn_2, inline_btn_3)
inline_kb_full.row(inline_btn_4, inline_btn_5)
inline_kb_full.row(inline_btn_3, inline_btn_6)
inline_kb_full.row(inline_btn_1, inline_btn_7)
inline_kb_full.row(inline_btn_8, inline_btn_9)
inline_kb_full.row(inline_btn_10, inline_btn_11)
inline_kb_full.row(inline_btn_12, inline_btn_13)