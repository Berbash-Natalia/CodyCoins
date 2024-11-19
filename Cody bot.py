from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
# Done! Congratulations on your new bot. You will find it at t.me/codydybot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.
#
# Use this token to access the HTTP API:
# 7625865990:AAEoRJOLQZsb8bl7wsTI4cKA_ijO9pAJiBA
# Keep your token secure and store it safely, it can be used by anyone to control your bot.
#
# For a description of the Bot API, see this page: https://core.telegram.org/bots/api

# Отправка изображения
async def send_image(update: Update, context):
    photo_url = "https://www.google.com/imgres?q=%D0%BA%D0%BE%D1%82&imgurl=https%3A%2F%2Fcdnn1.ukraina.ru%2Fimg%2F07e6%2F0c%2F02%2F1041436899_0%3A206%3A2905%3A1840_1920x0_80_0_0_c7022893b761781d76fe592010d14bd2.jpg&imgrefurl=https%3A%2F%2Fukraina.ru%2F20221202%2F1041437109.html&docid=CiWraHzdnIpAGM&tbnid=oumJ1Fg-rRTfFM&vet=12ahUKEwikjICupOiJAxUs0AIHHVs5E8QQM3oECGQQAA..i&w=1920&h=1079&hcb=2&ved=2ahUKEwikjICupOiJAxUs0AIHHVs5E8QQM3oECGQQAA"
    await update.message.reply_photo(photo=photo_url, caption="Вот ваше изображение!")


async def send_gif(update: Update, context):
    gif_url = "https://i.pinimg.com/originals/a6/42/72/a6427290d97d92343223643614c8ef80.gif"  # URL GIF
    await update.message.reply_animation(animation=gif_url, caption="Вот ваша GIF-анимация!")


# Обработка текстовых сообщений
async def handle_message(update: Update, context):
    text = update.message.text
    if "фото" in text.lower():
        await send_image(update, context)
    elif "гифка" in text.lower():
        await send_gif(update, context)
    else:
        await update.message.reply_text("Скажите 'фото' или 'гифка', чтобы получить результат.")


# Основная функция
def main():
    TOKEN = "7625865990:AAEoRJOLQZsb8bl7wsTI4cKA_ijO9pAJiBA"
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("image", send_image))
    app.add_handler(CommandHandler("gif", send_gif))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
