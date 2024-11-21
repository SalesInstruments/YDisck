import aiohttp
import json

async def post_request(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            response.raise_for_status()  # Проверка на HTTP ошибки
            return json.loads(await response.text())
        
        