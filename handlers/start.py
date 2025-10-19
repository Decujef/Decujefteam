from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from keyboard.main_menu import get_main_keyboard

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    user = message.from_user
    welcome_text = f"""
👋 Привет, {user.first_name}!

Я демонстрационный бот на aiogram!
Выберите действие ниже:
    """

    await message.answer(
        welcome_text,
        reply_markup=get_main_keyboard()
    )

@router.message(Command("help"))
async def cmd_help(message: Message):
    help_text = """
📚 <b>Доступные команды:</b>

/start - Запуск бота
/help - Помощь
/profile - Информация о вас
/stats - Статистика

🎛 <b>Или используйте кнопки меню!</b>
    """
    await message.answer(help_text)

@router.message(F.text == "👤 Профиль")
async def profile_button(message: Message):
    user = message.from_user

    profile_text = f"""
📊 <b>Ваш профиль:</b>

🆔 ID: <code>{user.id}</code>
👤 Имя: {user.first_name}
📛 Фамилия: {user.last_name or 'Не указана'}
🔗 Username: @{user.username or 'Не указан'}
🌐 Язык: {user.language_code or 'Не указан'}
    """

    await message.answer(profile_text)

@router.message(F.text == "📊 Статистика")
async def stats_button(message: Message):
    # Простая статистика для теста
    stats_text = """
📈 <b>Статистика бота:</b>

👥 Всего пользователей: 157
📨 Обработано сообщений: 1,342
🔄 Запросов за сегодня: 89
⚡ Активность: высокая

📊 <b>Ваша статистика:</b>
✅ Сообщений отправлено: 15
🕒 Первое использование: сегодня
🎯 Активность: регулярная
    """
    await message.answer(stats_text)

@router.message(F.text == "📞 Контакты")
async def contacts_button(message: Message):
    contacts_text = """
📞 <b>Наши контакты:</b>

📧 Email: support@example.com
🌐 Сайт: https://example.com
📱 Телеграм: @username

⏰ <i>Работаем круглосуточно!</i>
    """
    await message.answer(contacts_text)

@router.message(F.text == "🎲 Случайное число")
async def random_number_button(message: Message):
    import random
    number = random.randint(1, 100)
    await message.answer(f"🎯 Ваше случайное число: <b>{number}</b>")