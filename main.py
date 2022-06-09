from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5584038617:AAEQXKHLInxjd_IGY765SdHN8vgk-JDznkA").build()
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("difference", difference_command))
app.add_handler(CommandHandler("multiply", multiply_command))
app.add_handler(CommandHandler("division", division_command))
app.run_polling(stop_signals=None)