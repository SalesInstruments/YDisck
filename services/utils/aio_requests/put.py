import aiohttp

async def put(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.put(url, data=data) as response:
            if response.status != 201:
                error_message = await response.text()
                raise response(status_code=response.status, detail=f"Ошибка загрузки: {error_message}")