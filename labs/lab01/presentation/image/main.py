from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InputFile
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
import psycopg2
import logging

# Логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен Telegram
TOKEN = '7477964182:AAGrsvu1z8BsfmBeeGrzUmZcCB6AUh2T2V0'

# Параметры подключения к базе данных
DB_NAME = 'mydatabase'
DB_USER = 'myuser'
DB_PASSWORD = 'mypassword'
DB_HOST = 'localhost'
DB_PORT = '5433'

# Константы состояний для ConversationHandler
NAME, SEX, AGE, CITY, DESCRIPTION, PHOTO, SONG, CONFIRM = range(8)

def check_db_connection() -> str:
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.close()
        logger.info("Подключение к базе данных успешно установлено.")
        return "Подключение к базе данных успешно установлено. Код ответа: 200"
    except Exception as e:
        logger.error(f"Ошибка при подключении к базе данных: {e}")
        return f"Ошибка при подключении к базе данных: {e}"

def check_user_exists(user_id):
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE telegram_id = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user
    except Exception as e:
        logger.error(f"Ошибка при проверке пользователя: {e}")
        return None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.effective_user.id

    # Проверка подключения к базе данных
    db_status = check_db_connection()
    await update.message.reply_text(db_status)

    # Проверка, существует ли пользователь
    user = check_user_exists(user_id)
    if user:
        await update.message.reply_text("Вы уже зарегистрированы. Вот ваша анкета:")
        await show_profile(update, context)
        return ConversationHandler.END
    else:
        await update.message.reply_text("Введите ваше имя (слитно, на русском):")
        return NAME

#Cохранялка
async def save_data(user_id, name, sex, age, city, description, photo, song):
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (telegram_id, name, sex, age, city, description, photo, song) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (user_id, name, sex, age, city, description, photo, song)
        )
        conn.commit()
        cursor.close()
        conn.close()
        logger.info("Данные пользователя успешно сохранены.")
    except Exception as e:
        logger.error(f"Ошибка при сохранении данных: {e}")


#удалялка
async def delete_data(user_id):
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE telegram_id = %s", (user_id,))
        conn.commit()
        cursor.close()
        conn.close()
        logger.info("Данные пользователя успешно удалены.")
    except Exception as e:
        logger.error(f"Ошибка при удалении данных: {e}")

async def show_profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user = check_user_exists(user_id)
    if user:
        profile = (
            f"Ваш профиль:\n\n"
            f"Имя: {user[1]}\n"  # Проверьте правильность индексов
            f"Пол: {user[2]}\n"
            f"Возраст: {user[3]}\n"
            f"Город: {user[4]}\n"
            f"Описание: {user[5]}\n"
        )
        if user[6]:  # Фото
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=user[6])
        if user[7]:  # Песня
            await context.bot.send_audio(chat_id=update.effective_chat.id, audio=user[7])
        profile += f"Любимая песня: {user[7]}\n" if user[7] else ""
        await update.message.reply_text(profile)
    else:
        await update.message.reply_text("Профиль не найден. Пожалуйста, зарегистрируйтесь.")


async def change_profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.effective_user.id
    user = check_user_exists(user_id)
    if user:
        await delete_data(user_id)
        await update.message.reply_text("Ваши данные удалены из базы")
        return NAME
    else:
        await update.message.reply_text("Профиль не найден. Пожалуйста, зарегистрируйтесь.")
        return ConversationHandler.END




async def handle_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    name = update.message.text
    if not name.isalpha():  # Проверка на слитность и только алфавитные символы
        await update.message.reply_text("Имя должно быть слитным и содержать только буквы. Попробуйте снова:")
        return NAME
    context.user_data['name'] = name
    await update.message.reply_text("Выберите ваш пол:", reply_markup=ReplyKeyboardMarkup([['Мужской', 'Женский']], one_time_keyboard=True))
    return SEX

async def handle_sex(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    sex = update.message.text
    if sex not in ['Мужской', 'Женский']:
        await update.message.reply_text("Выберите пол из предложенных вариантов: Мужской или Женский.")
        return SEX
    context.user_data['sex'] = sex
    await update.message.reply_text("Введите ваш возраст (от 16 до 80 лет):")
    return AGE

async def handle_age(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    age = update.message.text
    if not age.isdigit() or not (16 <= int(age) <= 80):
        await update.message.reply_text("Возраст должен быть числом от 16 до 80. Попробуйте снова:")
        return AGE
    context.user_data['age'] = int(age)
    await update.message.reply_text("Введите ваш город (на русском языке):")
    return CITY

async def handle_city(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    city = update.message.text
    if not city.isalpha():  # Проверка на слитность и только алфавитные символы
        await update.message.reply_text("Город должен быть на русском языке и содержать только буквы. Попробуйте снова:")
        return CITY
    context.user_data['city'] = city
    await update.message.reply_text("Введите описание вашего профиля (на русском языке):")
    return DESCRIPTION

async def handle_description(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    description = update.message.text
    if not description.strip():
        await update.message.reply_text("Описание не должно быть пустым. Попробуйте снова:")
        return DESCRIPTION
    context.user_data['description'] = description
    await update.message.reply_text("Загрузите ваше фото. Не размещайте запрещенный контент.")
    return PHOTO

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    photo_file = update.message.photo[-1].file_id
    context.user_data['photo'] = photo_file
    await update.message.reply_text("Хотите добавить любимую песню? (да/нет)", reply_markup=ReplyKeyboardMarkup([['да', 'нет']], one_time_keyboard=True))
    return SONG

async def handle_song(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.text.lower() == 'да':
        await update.message.reply_text("Отправьте аудиофайл вашей любимой песни:")
        return CONFIRM
    else:
        context.user_data['song'] = None
        return await handle_confirmation(update, context)

async def handle_confirmation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if 'song' not in context.user_data:
        context.user_data['song'] = update.message.audio.file_id if update.message.audio else None

    user_id = update.effective_user.id
    await save_data(
        user_id,
        context.user_data['name'],
        context.user_data['sex'],
        context.user_data['age'],
        context.user_data['city'],
        context.user_data['description'],
        context.user_data['photo'],
        context.user_data['song']
    )
    profile = (
        f"Ваш профиль:\n\n"
        f"Имя: {context.user_data['name']}\n"
        f"Пол: {context.user_data['sex']}\n"
        f"Возраст: {context.user_data['age']}\n"
        f"Город: {context.user_data['city']}\n"
        f"Описание: {context.user_data['description']}\n"
    )
  



    await update.message.reply_text(profile, reply_markup=ReplyKeyboardRemove())
    if context.user_data['photo']:
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=context.user_data['photo'])
    if context.user_data['song']:
        await context.bot.send_audio(chat_id=update.effective_chat.id, audio=context.user_data['song'])
    return ConversationHandler.END

async def my_profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    user = check_user_exists(user_id)
    if user:
        await show_profile(update, context)
    else:
        await update.message.reply_text("Вы еще не зарегистрированы. Пожалуйста, используйте команду /start для регистрации.")

async def delete_profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    user = check_user_exists(user_id)
    if user:
        await delete_data(user_id)
        await update.message.reply_text("Ваш профиль был успешно удален.")
    else:
        await update.message.reply_text("Профиль не найден. Возможно, вы не были зарегистрированы.")

def main():
    app = Application.builder().token(TOKEN).build()

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            PHOTO: [MessageHandler(filters.PHOTO, handle_photo)],
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_name)],
            SEX: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_sex)],
            AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_age)],
            CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_city)],
            DESCRIPTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_description)],
            SONG: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_song), MessageHandler(filters.AUDIO, handle_confirmation)],
            CONFIRM: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_confirmation), MessageHandler(filters.AUDIO, handle_confirmation)]
        },
        fallbacks=[CommandHandler('start', start)]
    )

    app.add_handler(conversation_handler)
    app.add_handler(CommandHandler('myprofile', my_profile))
    app.add_handler(CommandHandler('deleteprofile', delete_profile))
    app.add_handler(CommandHandler('changeprofile', change_profile))

    logger.info("Бот запущен")
    app.run_polling()

if __name__ == '__main__':
    main()
