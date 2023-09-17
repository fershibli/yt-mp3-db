from pytube import YouTube
import os


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_audio_only()
    try:
        output_file = youtubeObject.download(output_path='./download')
        base, ext = os.path.splitext(output_file)
        os.rename(output_file, base + '.mp3')
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)
