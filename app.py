
from flask import Flask
import httpx
import asyncio
from random import randint

app = Flask(__name__)


async def get_image(client):
    random = randint(0, 300)
    # APIを叩いてコミック情報取得（I/O処理なのでawaitが必要）
    result = await client.get(f'http://xkcd.com/{random}/info.0.json')
    # 画像のURLのみ返す
    return result.json()['img']


@app.get('/async_api')
async def async_api():
    async with httpx.AsyncClient() as client:
        tasks = [get_image(client) for _ in range(10)]
        urls = await asyncio.gather(*tasks)

    html = ""
    for url in urls:
        html += f"<img src='{url}'><br><br>"
    return html


@app.get('/sync')
def sync():
    urls = []
    for _ in range(5):
        random = randint(0, 300)
        response = httpx.get(f'http://xkcd.com/{random}/info.0.json')
        urls.append(response.json()['img'])
    
    html = ""
    for url in urls:
        html += f"<img src='{url}'><br><br>"
    return html