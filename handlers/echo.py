from aiogram import Router, F
from aiogram.types import Message, ContentType
import random

router = Router()

# Обработка текстовых сообщений
@router.message(F.text)
async def echo_text(message: Message):
    user_text = message.text.lower()

    if user_text in ['привет', 'hello', 'hi']:
        await message.answer(f"👋 И тебе привет, {message.from_user.first_name}!")
    elif user_text in ['как дела?', 'как дела', 'how are you']:
        responses = ['Отлично!', 'Супер!', 'Всё хорошо!', 'Лучше всех!']
        await message.answer(random.choice(responses))
    elif user_text.startswith('скажи'):
        response = user_text.replace('скажи', '').strip()
        await message.answer(f"🔊 {response.capitalize()}!")
    else:
        await message.answer(f"🤖 Вы сказали: '{message.text}'")

# Обработка стикеров
@router.message(F.sticker)
async def echo_sticker(message: Message):
    await message.answer_sticker(message.sticker.file_id)
    await message.answer(f"📎 ID стикера: <code>{message.sticker.file_id}</code>")

# Обработка фото
@router.message(F.photo)
async def echo_photo(message: Message):
    await message.answer_photo(
        message.photo[-1].file_id,
        caption=f"📸 Красивое фото! ID: <code>{message.photo[-1].file_id}</code>"
    )

# Обработка голосовых сообщений
@router.message(F.voice)
async def echo_voice(message: Message):
    await message.answer("🎤 Голосовое сообщение получено!")
    await message.answer(f"⏱ Длительность: {message.voice.duration} сек")

# Обработка документов
@router.message(F.document)
async def echo_document(message: Message):
    file_name = message.document.file_name
    file_size = message.document.file_size

    await message.answer(
        f"📄 Документ получен!\n"
        f"📁 Имя: {file_name}\n"
        f"📏 Размер: {file_size} байт"
    )