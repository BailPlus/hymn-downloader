from abc import ABC, abstractmethod
from ..errors import PlatformNotSupport
import urllib.parse


class HymnPlatform(ABC):
    __domains__: list[str]  # 该平台绑定的域名列表

    def __init_subclass__(cls) -> None:
        if not hasattr(cls, '__domains__'):
            raise SyntaxError(f'请为{cls.__name__}平台类添加__domains__属性')

    @abstractmethod
    def get_mp3_url(self, url: str) -> str:
        """获取mp3链接"""

    @abstractmethod
    def get_lrc_url(self, url: str) -> str:
        """获取歌词链接"""

    @classmethod
    def from_url(cls, url: str) -> 'HymnPlatform':
        """根据url获取平台类"""
        for subclass in cls.__subclasses__():
            if urllib.parse.urlparse(url).hostname in subclass.__domains__:
                return subclass()
        else:
            raise PlatformNotSupport
