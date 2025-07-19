from dataclasses import dataclass
from httpx import AsyncClient
from .base import HymnPlatform
from ..errors import ParseFailed
import urllib.parse, asyncio

MUSIC_DETAIL_URL = 'https://share.lingtingmusic.com/api/v1/music/detail'


@dataclass(frozen=True)
class LingtingSongDetail:
    sone_name: str
    mp3_url: str
    lrc_url: str


class Lingting(HymnPlatform):
    __domains__ = ['share.lingtingmusic.com']

    async def _get_music_detail(self, url: str) -> LingtingSongDetail:
        async with AsyncClient() as client:
            res = (await client.get(MUSIC_DETAIL_URL, params={
                'songId': urllib.parse.parse_qs(
                    urllib.parse.urlparse(url)
                        .query
                )['song_id'][0]
            })).json()
        if not res.get('success'):
            raise ParseFailed
        return LingtingSongDetail(
            sone_name=res['data']['songName'],
            mp3_url=res['data']['audioLink'],
            lrc_url=res['data']['lyric']
        )

    async def get_mp3_url_async(self, url: str) -> str:
        return (await self._get_music_detail(url)).mp3_url

    async def get_lrc_url_async(self, url: str) -> str:
        return (await self._get_music_detail(url)).lrc_url

    def get_mp3_url(self, url: str) -> str:
        return asyncio.run(
            self.get_mp3_url_async(url)
        )
        

    def get_lrc_url(self, url: str) -> str:
        return asyncio.run(
            self.get_lrc_url_async(url)
        )
