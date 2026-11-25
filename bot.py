import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("About Glpay", callback_data="about")],
        [InlineKeyboardButton("How It Works", callback_data="how")],
        [InlineKeyboardButton("Support", callback_data="support")],
    ]
    await update.message.reply_text(
        "Welcome to Glpay_46bot.\n"
        "Your payment assistant on Telegram.\n"
        "Use the buttons below to learn more.",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Available commands:\n"
        "/start - Show the main menu\n"
        "/help - Show this help message"
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "about":
        await query.edit_message_text(
            "Glpay_46bot is a Telegram-based assistant designed to help users "
            "manage payment-related activities in a simple and clear way.",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Back", callback_data="back")]]
            ),
        )
    elif query.data == "how":
        await query.edit_message_text(
            "How it works:\n"
            "1. Use the menu to explore the bot.\n"
            "2. Follow the instructions provided.\n"
            "3. Contact support if you need assistance.",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Back", callback_data="back")]]
            ),
        )
    elif query.data == "support":
        await query.edit_message_text(
            "For assistance, please contact: support@example.com\n"
            "(Replace this with your actual support contact before submission.)",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Back", callback_data="back")]]
            ),
        )
    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton("About Glpay", callback_data="about")],
            [InlineKeyboardButton("How It Works", callback_data="how")],
            [InlineKeyboardButton("Support", callback_data="support")],
        ]
        await query.edit_message_text(
            "Welcome to Glpay_46bot.\n"
            "Your payment assistant on Telegram.\n"
            "Use the buttons below to learn more.",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )


def main():
    if not TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN is not set.")
        return

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button_handler))

    logger.info("Bot starting...")
    app.run_polling()


if __name__ == "__main__":
    main()
