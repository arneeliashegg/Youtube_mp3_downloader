from pytube import YouTube
import os

url = YoutTube(str(input("Youtube Video URL: ")))
vid = url.streams.filter(only_audio=True).first()
out_file = vid.download(output_path=".")
base, ext = os.path.splitext(out_file)
new_file = base + ".mp3"
os.rename(out_file, new_file)
print(url.title + " has been successfully downloaded.")

