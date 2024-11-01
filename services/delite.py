import yadisk

async def delite_file(path:str):
    y = yadisk.AsyncClient(token="y0_AgAAAAA2bkLJAAyZhgAAAAEUUNqgAABEIQCFPARHka_SA_Yc4rWJuWVhpQ")

    await y.remove(f"/{path}", permanently=True)