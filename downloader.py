import math
import logging
from config import TOKEN
from pytube import YouTube
from pytube.exceptions import AgeRestrictedError, RegexMatchError
from asyncio.exceptions import TimeoutError
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from text import start_text, send_video_text, error_text_start, send_audio_text, \
    download_video_text, download_audio_text, wishes_audio, age_error, not_link_text, \
    mystery_error, size_problem, cutting_start, wishes_video

from moviepy.editor import *


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO, filename="youtube_bot.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")


@dp.message_handler(commands=['start'])
async def start_message(message: Message):
    try:
        logging.info(f"{message.from_user.full_name, message.text, message.from_user.username}")
        await message.answer(start_text.format(message.from_user))
    except Exception as error:
        logging.error(error, exc_info=True)
        await bot.send_message(message.from_user.id, text=error_text_start)


@dp.message_handler(content_types="text")
async def video(message: Message):
    try:
        request = message.text
        await bot.send_message(message.from_user.id, download_video_text)
        link = f"{request}"
        logging.info(f"{message.from_user.full_name, message.from_user.username, link}")
        yt = YouTube(link)
        file = yt.streams.get_highest_resolution().download()
        file_size = os.path.getsize(file)
        await bot.send_message(message.from_user.id, download_audio_text)
        audio_clip = AudioFileClip(file)
        audio_clip.write_audiofile("audio.mp3")
        audio_clip_size = os.path.getsize("audio.mp3")
        if audio_clip_size > 51380224:
            audio_clip = AudioFileClip("audio.mp3")
            audio_clip.write_audiofile("audio.mp3")
            with AudioFileClip(filename="audio.mp3") as audio:
                file_name = os.path.splitext(p=os.path.basename("audio.mp3"))[0]
                numbers_of_segments = math.floor(audio_clip.duration // 4)
                for i in range(numbers_of_segments):
                    start = i * math.floor(audio_clip.duration // 4)
                    end = (i + 1) * math.floor(audio_clip.duration // 4)
                    current_segment = audio.subclip(t_start=start, t_end=end)
                    final_file_name = file_name + '_' + str(i + 1) + '.mp3'
                    output_filename = os.path.join('./', final_file_name)
                    current_segment.write_audiofile(filename=output_filename, codec="libx264")
                    await bot.send_audio(message.from_user.id, open(final_file_name, "rb"))
                    os.remove(final_file_name)
        await bot.send_message(message.from_user.id, send_audio_text)
        await bot.send_audio(message.from_user.id, open("audio.mp3", "rb"))
        await bot.send_message(message.from_user.id, wishes_audio)
        os.remove("audio.mp3")

        if file_size <= 50331648: # меньше или равен 48мб
            await bot.send_message(message.from_user.id, send_video_text)
            await bot.send_video(message.from_user.id, open(file, "rb"))
            await bot.send_message(message.from_user.id, wishes_video)

        elif file_size >= 51380224 and file_size <= 136314880: # больше или равен 49мб и меньше или равен 130мб
            await bot.send_message(message.from_user.id, size_problem)
            await bot.send_message(message.from_user.id, cutting_start)
            video_path = file
            with VideoFileClip(filename=video_path, audio=True) as video:
                file_name = os.path.splitext(p=os.path.basename(video_path))[0]
                numbers_of_segments = math.floor(video.duration // 8)
                for i in range(numbers_of_segments):
                    start = i * math.floor(video.duration // 8)
                    end = (i + 1) * math.floor(video.duration // 8)
                    current_segment = video.subclip(t_start=start, t_end=end)
                    final_file_name = file_name + '_' + str(i + 1) + '.mp4'
                    output_filename = os.path.join('./', final_file_name)
                    current_segment.write_videofile(filename=output_filename, codec="libx264", fps=60)
                    await bot.send_video(message.from_user.id, open(final_file_name, "rb"))
                    os.remove(final_file_name)
            await bot.send_message(message.from_user.id, wishes_video)
            os.remove(file)

        elif file_size >= 136314880 and file_size <= 209715200: # больше или равен 130мб и меньше или равен 200мб
            await bot.send_message(message.from_user.id, size_problem)
            await bot.send_message(message.from_user.id, cutting_start)
            video_path = file
            with VideoFileClip(filename=video_path, audio=True) as video:
                file_name = os.path.splitext(p=os.path.basename(video_path))[0]
                numbers_of_segments = math.floor(video.duration // 12)
                for i in range(numbers_of_segments):
                    start = i * math.floor(video.duration // 12)
                    end = (i + 1) * math.floor(video.duration // 12)
                    current_segment = video.subclip(t_start=start, t_end=end)
                    final_file_name = file_name + '_' + str(i + 1) + '.mp4'
                    output_filename = os.path.join('./', final_file_name)
                    current_segment.write_videofile(filename=output_filename, codec="libx264", fps=60)
                    await bot.send_video(message.from_user.id, open(final_file_name, "rb"))
                    os.remove(final_file_name)
            await bot.send_message(message.from_user.id, wishes_video)
            os.remove(file)

        elif file_size >= 209715200 and file_size <= 262144000: # больше или равен 200мб и меньше или равен 250мб
            await bot.send_message(message.from_user.id, size_problem)
            await bot.send_message(message.from_user.id, cutting_start)
            video_path = file
            with VideoFileClip(filename=video_path, audio=True) as video:
                file_name = os.path.splitext(p=os.path.basename(video_path))[0]
                numbers_of_segments = math.floor(video.duration // 16)
                for i in range(numbers_of_segments):
                    start = i * math.floor(video.duration // 16)
                    end = (i + 1) * math.floor(video.duration // 16)
                    current_segment = video.subclip(t_start=start, t_end=end)
                    final_file_name = file_name + '_' + str(i + 1) + '.mp4'
                    output_filename = os.path.join('./', final_file_name)
                    current_segment.write_videofile(filename=output_filename, codec="libx264", fps=60)
                    await bot.send_video(message.from_user.id, open(final_file_name, "rb"))
                    os.remove(final_file_name)
            await bot.send_message(message.from_user.id, wishes_video)
            os.remove(file)

        elif file_size >= 262144000 and file_size <= 314572800: # больше или равен 250мб и меньше или равен 300мб
            await bot.send_message(message.from_user.id, size_problem)
            await bot.send_message(message.from_user.id, cutting_start)
            video_path = file
            with VideoFileClip(filename=video_path, audio=True) as video:
                file_name = os.path.splitext(p=os.path.basename(video_path))[0]
                numbers_of_segments = math.floor(video.duration // 18)
                for i in range(numbers_of_segments):
                    start = i * math.floor(video.duration // 18)
                    end = (i + 1) * math.floor(video.duration // 18)
                    current_segment = video.subclip(t_start=start, t_end=end)
                    final_file_name = file_name + '_' + str(i + 1) + '.mp4'
                    output_filename = os.path.join('./', final_file_name)
                    current_segment.write_videofile(filename=output_filename, codec="libx264", fps=60)
                    await bot.send_video(message.from_user.id, open(final_file_name, "rb"))
                    os.remove(final_file_name)
            await bot.send_message(message.from_user.id, wishes_video)
            os.remove(file)

        elif file_size >= 314572800 and file_size <= 367001600: # больше или равен 300мб и меньше или равен 350мб
            await bot.send_message(message.from_user.id, size_problem)
            await bot.send_message(message.from_user.id, cutting_start)
            video_path = file
            with VideoFileClip(filename=video_path, audio=True) as video:
                file_name = os.path.splitext(p=os.path.basename(video_path))[0]
                numbers_of_segments = math.floor(video.duration // 20)
                for i in range(numbers_of_segments):
                    start = i * math.floor(video.duration // 20)
                    end = (i + 1) * math.floor(video.duration // 20)
                    current_segment = video.subclip(t_start=start, t_end=end)
                    final_file_name = file_name + '_' + str(i + 1) + '.mp4'
                    output_filename = os.path.join('./', final_file_name)
                    current_segment.write_videofile(filename=output_filename, codec="libx264", fps=60)
                    await bot.send_video(message.from_user.id, open(final_file_name, "rb"))
                    os.remove(final_file_name)
            await bot.send_message(message.from_user.id, wishes_video)
            os.remove(file)

        elif file_size >= 367001600 and file_size <= 419430400: # больше или равен 350мб и меньше или равен 400мб
            await bot.send_message(message.from_user.id, size_problem)
            await bot.send_message(message.from_user.id, cutting_start)
            video_path = file
            with VideoFileClip(filename=video_path, audio=True) as video:
                file_name = os.path.splitext(p=os.path.basename(video_path))[0]
                numbers_of_segments = math.floor(video.duration // 22)
                for i in range(numbers_of_segments):
                    start = i * math.floor(video.duration // 22)
                    end = (i + 1) * math.floor(video.duration // 22)
                    current_segment = video.subclip(t_start=start, t_end=end)
                    final_file_name = file_name + '_' + str(i + 1) + '.mp4'
                    output_filename = os.path.join('./', final_file_name)
                    current_segment.write_videofile(filename=output_filename, codec="libx264", fps=60)
                    await bot.send_video(message.from_user.id, open(final_file_name, "rb"))
                    os.remove(final_file_name)
            await bot.send_message(message.from_user.id, wishes_video)
            os.remove(file)

        elif file_size >= 419430400 and file_size <= 471859200: # больше или равен 400мб и меньше или равен 450мб
            await bot.send_message(message.from_user.id, size_problem)
            await bot.send_message(message.from_user.id, cutting_start)
            video_path = file
            with VideoFileClip(filename=video_path, audio=True) as video:
                file_name = os.path.splitext(p=os.path.basename(video_path))[0]
                numbers_of_segments = math.floor(video.duration // 24)
                for i in range(numbers_of_segments):
                    start = i * math.floor(video.duration // 24)
                    end = (i + 1) * math.floor(video.duration // 24)
                    current_segment = video.subclip(t_start=start, t_end=end)
                    final_file_name = file_name + '_' + str(i + 1) + '.mp4'
                    output_filename = os.path.join('./', final_file_name)
                    current_segment.write_videofile(filename=output_filename, codec="libx264", fps=60)
                    await bot.send_video(message.from_user.id, open(final_file_name, "rb"))
                    os.remove(final_file_name)
            await bot.send_message(message.from_user.id, wishes_video)
            os.remove(file)

        elif file_size >= 471859200 and file_size <= 524288000: # больше или равен 450мб и меньше или равен 500мб
            await bot.send_message(message.from_user.id, size_problem)
            await bot.send_message(message.from_user.id, cutting_start)
            video_path = file
            with VideoFileClip(filename=video_path, audio=True) as video:
                file_name = os.path.splitext(p=os.path.basename(video_path))[0]
                numbers_of_segments = math.floor(video.duration // 26)
                for i in range(numbers_of_segments):
                    start = i * math.floor(video.duration // 26)
                    end = (i + 1) * math.floor(video.duration // 26)
                    current_segment = video.subclip(t_start=start, t_end=end)
                    final_file_name = file_name + '_' + str(i + 1) + '.mp4'
                    output_filename = os.path.join('./', final_file_name)
                    current_segment.write_videofile(filename=output_filename, codec="libx264", fps=60)
                    await bot.send_video(message.from_user.id, open(final_file_name, "rb"))
                    os.remove(final_file_name)
            await bot.send_message(message.from_user.id, wishes_video)
            os.remove(file)

        elif file_size >= 524288000 and file_size <= 576716800: # больше или равен 500мб и меньше или равен 550мб
            await bot.send_message(message.from_user.id, size_problem)
            await bot.send_message(message.from_user.id, cutting_start)
            video_path = file
            with VideoFileClip(filename=video_path, audio=True) as video:
                file_name = os.path.splitext(p=os.path.basename(video_path))[0]
                numbers_of_segments = math.floor(video.duration // 28)
                for i in range(numbers_of_segments):
                    start = i * math.floor(video.duration // 28)
                    end = (i + 1) * math.floor(video.duration // 28)
                    current_segment = video.subclip(t_start=start, t_end=end)
                    final_file_name = file_name + '_' + str(i + 1) + '.mp4'
                    output_filename = os.path.join('./', final_file_name)
                    current_segment.write_videofile(filename=output_filename, codec="libx264", fps=60)
                    await bot.send_video(message.from_user.id, open(final_file_name, "rb"))
                    os.remove(final_file_name)
            await bot.send_message(message.from_user.id, wishes_video)
            os.remove(file)

    except OSError:
        pass
    except AgeRestrictedError:
        logging.error(RegexMatchError, exc_info=True)
        await bot.send_message(message.from_user.id, age_error)
    except RegexMatchError:
        logging.error(RegexMatchError, exc_info=True)
        await bot.send_message(message.from_user.id, not_link_text)
    except TimeoutError:
        logging.error(RegexMatchError, exc_info=True)
    except Exception as error:
        logging.error(error, exc_info=True)
        await bot.send_message(message.from_user.id, text=mystery_error)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, timeout=False)