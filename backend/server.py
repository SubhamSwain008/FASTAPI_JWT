from typing import Union

from fastapi import FastAPI
from routes.routes import Rout
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from config.db import client
from contextlib import asynccontextmanager
load_dotenv()

@asynccontextmanager
async def Lifespan(app: FastAPI):
    # Startup: runs before the app starts serving
    client.jwt_data.users.create_index("username", unique=True)
    print("MongoDB username index ensured")
    yield
    # Shutdown: runs when app is shutting down
    client.close()
    print("MongoDB connection closed")

app = FastAPI(lifespan=Lifespan) # type: ignore
app.include_router(Rout)

url=os.getenv("CLIENT_URL")

origins = [
    url
  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # pyright: ignore[reportArgumentType]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
