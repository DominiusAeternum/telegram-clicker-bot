from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7323206854:AAEO8LuQkEEMcbjq8yRhxMPIRGHCFOO1H8E"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Играть 🎮", web_app=WebAppInfo(url="https://admirable-sfogliatella-2b66f2.netlify.app"))]
    ]
    await update.message.reply_text("Привет! Нажми, чтобы играть 👇", reply_markup=InlineKeyboardMarkup(keyboard))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
