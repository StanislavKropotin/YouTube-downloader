# YouTube Donwnloader

An asynchronous bot written in the AIogram + MovePy library. 

I didn’t deploy it on the hosting because of the video processing (cutting into parts based on the weight of the file due to the limitation on sending 50MB files by bots).

The code loads the video, separates the audio into a separate file (saving the audio in the video itself)

And, depending on the file size, it cuts and sends - an approximate video of each segment - about 3 minutes

In general, in order to download the audio track of a video and the video itself for yourself, you can use the file “downloader video_audio.py” - 
since all other libraries and files are needed only to reduce the size of the file.

I do not attach the config.py file with the bot token

What to do to make it work:

1) Dependencies need to be installed (pip install -r requirements.txt)

2) Go to file “downloader video_audio.py”

3) Insert the YouTube link between the quotes in the "link" variable

4) The video will begin downloading, after which the file "audio.mp3" will be created

5) Listen and watch!
