from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message
from config import Config

router = Router()

# Фильтр для админов
def is_admin(user_id: int) -> bool:
    return user_id in Config.ADMIN_IDS

@router.message(Command("stats"), F.from_user.id.in_(Config.ADMIN_IDS))
async def cmd_stats(message: Message):
    stats_text = """
📊 <b>Статистика бота (админ)</b>

👥 Пользователей: 100
📨 Сообщений: 1000
🔄 Запросов: 500
    """
    await message.answer(stats_text)

@router.message(Command("broadcast"), F.from_user.id.in_(Config.ADMIN_IDS))
async def cmd_broadcast(message: Message):
    await message.answer("📢 Режим рассылки. Отправьте сообщение для рассылки.")

@router.message(F.from_user.id.in_(Config.ADMIN_IDS), F.reply_to_message)
async def handle_broadcast(message: Message):
    if "рассылка" in message.text.lower():
        # Здесь будет логика рассылки
        await message.answer("✅ Рассылка начата!")