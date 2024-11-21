from services.utils.aio_requests.post import post_request
from config import URL_AUTH

async def check_token(token:str):
    url = f'{URL_AUTH}/auth/verify-token'
    return await post_request(url, {"token": token})