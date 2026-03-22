import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("البوت شغال ✅")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text:
        await update.message.reply_text(update.message.text)
    else:
        await update.message.reply_text("ارسل نص فقط")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, echo))

print("Bot started")
app.run_polling()
