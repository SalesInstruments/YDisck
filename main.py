import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import (engine, 
                      Base, 
                      init_models)
from routers.YDiskRouter import router as router

app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:5173",
#     "http://localhost:3000"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["GET"],
#     allow_headers=["*"],
# )
# Base.metadata.create_all(bind=engine)

# @app.on_event("startup")
# async def on_startup():
#     await init_models()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)