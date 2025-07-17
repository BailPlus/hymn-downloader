import urllib.parse

MP3URL = 'https://resource.lingtingmusic.com/music/voice/{song_id}.mp3'
LRCURL = 'https://resource.lingtingmusic.com/music/voice/{song_id}.lrc'


async def get_music(url: str):
    return MP3URL.format(
        song_id=urllib.parse.parse_qs(
            urllib.parse.urlparse(url)
                .query
            )['song_id'][0]
        )

