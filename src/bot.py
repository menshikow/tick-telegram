import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from handlers import add, adddesc, done, list, start, delete, help, clear, fallback
from config import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    app = Application.builder().token(config.BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start.start_handler))
    app.add_handler(CommandHandler("help", help.help_handler))
    app.add_handler(CommandHandler("add", add.add_handler))
    app.add_handler(CommandHandler("list", list.list_handler))
    app.add_handler(CommandHandler("done", done.done_handler))
    app.add_handler(CommandHandler("adddesc", adddesc.add_description_handler))
    app.add_handler(CommandHandler("delete", delete.delete_handler))
    app.add_handler(CommandHandler("clear", clear.clear_handler))

    # fallback handler for any unrecognized text
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, fallback.unknown_handler)
    )

    logger.info("bot is running...")
    try:
        app.run_polling(allowed_updates=[])
    except Exception as e:
        logger.error(f"bot crashed: {e}", exc_info=True)


if __name__ == "__main__":
    main()
