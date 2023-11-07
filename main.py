from pytube import YouTube
import os

# API Documentation: https://pytube.io/en/latest/

PATH = 'Downloaded_Videos'
if not os.path.exists(PATH):
    os.makedirs(PATH)

# ONLY CHANGE THIS URL
url = 'https://www.youtube.com/watch?v=mYDBDd3N_IE&ab_channel=Lulunolly'

yt = YouTube(url)
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path='Downloaded_Videos')

#  --------------------USE CODE BELOW ONLY FOR SPECIFIC VIDEO SELECTING ----------------------------

# Used to see what versions of the video that can be downloaded
# for stream in yt.streams.filter(file_extension='mp4').filter(type='video'):
#     print(stream)

# Change the itag value to the one you want to download
# Comment the code out below so it doesn't run when you looking for video's itag

# itag = 18
# stream = yt.streams.get_by_itag(itag)
# stream.download(output_path='Downloaded_Videos')
print('Finished Downloading')