from .base import HymnPlatform
import urllib.parse

MP3URL = 'https://resource.lingtingmusic.com/music/voice/{song_id}.mp3'
LRCURL = 'https://resource.lingtingmusic.com/music/voice/{song_id}.lrc'

class Lingting(HymnPlatform):
    __domains__ = ['share.lingtingmusic.com']

    def get_mp3_url(self, url: str) -> str:
        return MP3URL.format(
            song_id=urllib.parse.parse_qs(
                urllib.parse.urlparse(url)
                    .query
                )['song_id'][0]
            )

    def get_lrc_url(self, url: str) -> str:
        return LRCURL.format(
            song_id=urllib.parse.parse_qs(
                urllib.parse.urlparse(url)
                    .query
                )['song_id'][0]
            )
