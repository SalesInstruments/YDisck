import aiohttp

async def delete(url: str, headers: dict, params: dict):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                print(f"Ошибка: {response.status}")
                print(await response.text())
                return None