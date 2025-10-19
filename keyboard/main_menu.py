from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

def get_main_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.add(KeyboardButton(text="👤 Профиль"))
    builder.add(KeyboardButton(text="📊 Статистика"))
    builder.add(KeyboardButton(text="🎲 Случайное число"))
    builder.add(KeyboardButton(text="📞 Контакты"))

    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

def get_inline_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.add(InlineKeyboardButton(text="🌐 Сайт", url="https://example.com"))
    builder.add(InlineKeyboardButton(text="📱 Канал", url="https://t.me/example"))
    builder.add(InlineKeyboardButton(text="🔄 Обновить", callback_data="refresh"))
    builder.add(InlineKeyboardButton(text="❌ Закрыть", callback_data="close"))

    builder.adjust(2)
    return builder.as_markup()

# Обработка callback-ов
from aiogram import Router, F
from aiogram.types import CallbackQuery

callback_router = Router()

@callback_router.callback_query(F.data == "refresh")
async def refresh_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        "🔄 Данные обновлены!",
        reply_markup=get_inline_keyboard()
    )
    await callback.answer()

@callback_router.callback_query(F.data == "close")
async def close_callback(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()