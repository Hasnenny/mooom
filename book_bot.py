
from googlesearch import search
import telebot
import time

TOKEN = "5021162535:AAFgm4JangIEMR3vQ1TJK2bqhTarWeqXR0Q"
CHANNEL_USERNAME = "mktbthmss"
REQUIRED_CHANNEL = f"https://t.me/{CHANNEL_USERNAME}"

ADMINS = [8107515446]  # ايديات المشرفين
bot_status = {"active": True}

bot = telebot.TeleBot(TOKEN)

welcome_text = """📚 مرحبًا بك في بوت الكتب المتقدم!

🔍 للبحث عن أي كتاب، فقط أرسل اسم الكتاب أو جزء منه.

مثال:
كتاب لانك الله
رواية غربة الياسمين
الجنة المفقوده
"""

welcome_markup = telebot.types.InlineKeyboardMarkup()
welcome_markup.add(
    telebot.types.InlineKeyboardButton(text="📚 مكتبة الكتب", url="https://t.me/mktbthmss")
)

source_markup = telebot.types.InlineKeyboardMarkup()
source_markup.add(
    telebot.types.InlineKeyboardButton(text="**_BOT library_**", url="https://t.me/mktbahbot"),
    telebot.types.InlineKeyboardButton(text="**_Book library_**", url="https://t.me/mktbthmss")
)

def check_subscription(user_id):
    try:
        member = bot.get_chat_member(f"@{CHANNEL_USERNAME}", user_id)
        return member.status in ["member", "creator", "administrator"]
    except:
        return False

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if not bot_status["active"]:
        bot.send_message(message.chat.id, "❌ البوت حالياً تحت الصيانة.")
        return
    if not check_subscription(message.from_user.id):
        bot.send_message(message.chat.id, f"🚫 يجب عليك الاشتراك أولاً: {REQUIRED_CHANNEL}")
        return
    bot.send_message(message.chat.id, welcome_text, reply_markup=welcome_markup)

@bot.message_handler(commands=['search'])
def ask_book(message):
    if not bot_status["active"]:
        bot.send_message(message.chat.id, "❌ البوت تحت الصيانة.")
        return
    if not check_subscription(message.from_user.id):
        bot.send_message(message.chat.id, f"🚫 يجب عليك الاشتراك أولاً: {REQUIRED_CHANNEL}")
        return
    msg = bot.send_message(message.chat.id, "📘 اكتب اسم الكتاب الذي تبحث عنه:")
    bot.register_next_step_handler(msg, search_book)

def search_book(message):
    time.sleep(5)
    query = f"{message.text} تحميل PDF"
    try:
        results = list(search(query, num_results=5, lang="ar"))
        if results:
            reply = "🔍 روابط البحث:

"
            for idx, link in enumerate(results, 1):
                reply += f"{idx}. 🔗 {link}
"
            reply += "
📄 عذرًا لا يمكنني إرسال الملف مباشرة لهذا الكتاب حالياً."
            bot.send_message(message.chat.id, reply)
        else:
            bot.send_message(message.chat.id, "❌ لم أجد نتائج.")
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ خطأ أثناء البحث:
{e}")

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    text = message.text.lower()
    if any(word in text for word in ["سورس", "source", "السورس"]):
        bot.send_message(message.chat.id, "- 𝘞𝘦𝘭𝘤𝘰𝘮𝘦 𝘵𝘰 𝘵𝘩𝘦 𝘣𝘭𝘢𝘤𝘬 𝘴𝘰𝘶𝘳𝘤𝘦 .", reply_markup=source_markup)
    elif text == "تشغيل" and message.from_user.id in ADMINS:
        bot_status["active"] = True
        bot.send_message(message.chat.id, "✅ تم تفعيل البوت.")
    elif text == "تعطيل" and message.from_user.id in ADMINS:
        bot_status["active"] = False
        bot.send_message(message.chat.id, "❌ تم تعطيل البوت.")

bot.infinity_polling(skip_pending=True)
