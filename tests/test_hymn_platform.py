from unittest import TestCase
from src.adapter.base import HymnPlatform
from src.adapter import Izanmei, Lingting
from src.errors import PlatformNotSupport

IZM_EXAMPLE_URL = 'https://www.izanmei.com/song/13597.html'
IZM_SHARE_EXAMPLE_URL = 'https://izanmei.net/s13597'
LINGTING_EXAMPLE_URL = 'https://share.lingtingmusic.com/song?song_id=26968'


class TestHymnPlatform(TestCase):
    def test_from_url(self):
        self.assertIsInstance(HymnPlatform.from_url(IZM_EXAMPLE_URL), Izanmei)
        self.assertIsInstance(HymnPlatform.from_url(IZM_SHARE_EXAMPLE_URL), Izanmei)
        self.assertIsInstance(HymnPlatform.from_url(LINGTING_EXAMPLE_URL), Lingting)
        self.assertRaises(PlatformNotSupport, HymnPlatform.from_url, 'https://www.baidu.com')
    
    def test_izm_get_mp3(self):
        self.assertEqual(
            HymnPlatform.from_url(IZM_EXAMPLE_URL).get_mp3_url(IZM_EXAMPLE_URL),
            'https://play.izanmei.net/song/p/13597.mp3'
        )
        self.assertEqual(
            HymnPlatform.from_url(IZM_SHARE_EXAMPLE_URL).get_mp3_url(IZM_SHARE_EXAMPLE_URL),
            'https://play.izanmei.net/song/p/13597.mp3'
        )
    
    def test_lt_get_mp3(self):
        self.assertEqual(
            HymnPlatform.from_url(LINGTING_EXAMPLE_URL).get_mp3_url(LINGTING_EXAMPLE_URL),
            'https://resource.lingtingmusic.com/music/voice/26968.mp3'
        )
    
    def test_izm_get_lrc(self):
        return
        self.assertEqual(
            HymnPlatform.from_url(IZM_EXAMPLE_URL).get_lrc_url(IZM_EXAMPLE_URL),
            'https://www.izanmei.com/song/13597.lrc'
        )
    
    def test_lt_get_lrc(self):
        return
        self.assertEqual(
            HymnPlatform.from_url(LINGTING_EXAMPLE_URL).get_lrc_url(LINGTING_EXAMPLE_URL),
            'https://share.lingtingmusic.com/song?song_id=26968'
        )
