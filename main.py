from pytube import YouTube
import os

# API Documentation: https://pytube.io/en/latest/

PATH = 'Downloaded_Videos'
if not os.path.exists(PATH):
    os.makedirs(PATH)

url = 'https://www.youtube.com/watch?v=9bZkp7q19f0&ab_channel=officialpsy'
yt = YouTube(url)

# Used to see what versions of the video that can be downloaded
for stream in yt.streams.filter(file_extension='mp4').filter(type='video'):
    print(stream)

# Change the itag value to the one you want to download
# Comment the code out below so it doesn't run when you looking for video's itag

itag = 18
stream = yt.streams.get_by_itag(itag)
stream.download(output_path='Downloaded_Videos')
print('Finished Downloading')