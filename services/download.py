from pytube import YouTube
import os


def downloadMusic(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_audio_only()
    try:
        output_file = youtubeObject.download(output_path='./download')
        base, ext = os.path.splitext(output_file)
        os.rename(output_file, base + '.mp3')
    except:
        print("An error has occurred")
        return False
    print("Download is completed successfully")
    return True
