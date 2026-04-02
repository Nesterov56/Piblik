from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

TOKEN = "8651674176:AAE8b2GouLizZaVbPlkVNnEGi1sDImQ9dJk"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот 🙂 Напиши 'привет' или 'пока'")

# Обычные сообщения
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "привет" in text:
        await update.message.reply_text("Привет!")
    if "пока" in text:
        await update.message.reply_text("Пока!")

app = ApplicationBuilder().token(TOKEN).build() #fdfsfdfsf

# 👇 ВАЖНО: добавляем обработчик команды
app.add_handler(CommandHandler("start", start))

app.add_handler(MessageHandler(filters.TEXT, handle_message))

print("Бот запущен...")
app.run_polling()
