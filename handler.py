from aiogram import types
from misc import *
from exceptions import NotFoundTrack
from serializer import Track


@dp.message_handler(content_types=[types.ContentType.VOICE])
async def recognize_song(message: types.Message):
    voice = await message.voice.download()
    info = await shazam.recognize_song(voice.name)
    try:
        serialized_track = Track(info)
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=serialized_track.image,
                             caption=f"Трек: {serialized_track.subtitle} - {serialized_track.title}\n"
                                     f"[Слушать в Apple Music]({serialized_track.appleMusic_url})\n",
                             parse_mode='Markdown')
    except NotFoundTrack:
        await bot.send_message(chat_id=message.from_user.id, text='Не удалось найти песню. Попробуйте еще раз.')
