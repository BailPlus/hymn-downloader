from httpx import AsyncClient
from bs4 import BeautifulSoup
import asyncio

async def get_html(url: str) -> str:
    async with AsyncClient() as client:
        resp = await client.get(url, follow_redirects=True)
        resp.raise_for_status()
        return resp.text

def get_mp3_url(dom: BeautifulSoup) -> str:
    try:
        return dom.find('ul', class_="sm2-playlist-bd").find('a').get('href')
    except AttributeError as e:
        breakpoint()
        raise ParseFailed

async def get_music(url: str) -> str:
    return get_mp3_url(
        BeautifulSoup(
            await get_html(url)
        )
    )

def main():
    pass


class ParseFailed(RuntimeError):
    def __init__(self, msg='解析失败'):
        self.msg = msg
    def __str__(self):
        return self.msg


if __name__ == "__main__":
    main()
