#downloading youtube video


import yt_dlp

#enter the url
url= input("enter the url of the youtube video")

ydl_opts={}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
print("video downloaded successfully")