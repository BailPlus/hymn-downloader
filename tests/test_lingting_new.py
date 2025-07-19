from unittest import TestCase
from src.adapter.lingting import Lingting

TEST_URL = 'https://share.lingtingmusic.com/song?song_id=27255'

class TestLingtingNew(TestCase):
    def test_get_mp3_url(self):
        lt = Lingting()
        self.assertEqual(
            lt.get_mp3_url(TEST_URL),
            'https://resource.lingtingmusic.com/music/voice/ade520512da6d6178cb17e64ad0df84b.mp3'
        )
    
    def test_get_lrc_url(self):
        lt = Lingting()
        self.assertEqual(
            lt.get_lrc_url(TEST_URL),
            'https://listen-to-heart-1320693856.cos.ap-nanjing.myqcloud.com/music/voice/a914a19eabcda95d8ba6ae68f6b9b787.lrc'
        )
