from pytube import YouTube
from moviepy.editor import *

link = "" # Insert your link here
yt = YouTube(link)
file = yt.streams.get_highest_resolution().download()
audio_clip = AudioFileClip(file)
audio_clip.write_audiofile("audio.mp3")
audio_clip_size = os.path.getsize("audio.mp3")
