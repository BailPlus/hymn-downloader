from bs4 import BeautifulSoup
from .base import HymnPlatform
from ..errors import ParseFailed
import httpx

class Izanmei(HymnPlatform):
    __domains__ = ['izanmei.net', 'www.izanmei.com']
    MP3_URL_TEMPLATE = 'https://play.izanmei.net/song/p/{id}.mp3'

    def get_mp3_url_directly(self, url: str) -> str:
        return self.MP3_URL_TEMPLATE.format(id=url.split('/')[-1])

    def get_lrc_url(self, url: str) -> str:
        raise NotImplementedError

    def get_html(self, url: str) -> str:
        return httpx.get(url, follow_redirects=True).raise_for_status().text

    def get_mp3_url(self, url: str) -> str:
        dom = BeautifulSoup(self.get_html(url))
        try:
            return dom.find('ul', class_="sm2-playlist-bd").find('a').get('href') # type: ignore
        except AttributeError as e:
            raise ParseFailed
