from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

token = "7150796538:AAEzHq26ikOsSeL1GpVMzbvEFLsUyeU2N_Q"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Salom! Men sizning yangi botingizman.')

def main() -> None:
    # Bot tokenini o'zgartiring
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling()

if __name__ == '__main__':
    main()
