from pytube import Playlist
from models import PlaylistEntity


def fetchPlaylist(link):
    pytubePlaylist = Playlist(link)
    PlaylistEntity(
        url=link,
        name=pytubePlaylist.title,
        content=pytubePlaylist.video_urls,
    )
