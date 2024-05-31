from contextlib import asynccontextmanager
from fastapi import FastAPI

from config import DSN
from modules import database
from modules.api import router


@asynccontextmanager
async def lifespan(_: FastAPI):
    await database.PhoneSessionDB.connect(DSN)
    yield
    await database.PhoneSessionDB.close()

app = FastAPI(lifespan=lifespan) 
app.include_router(router.router)
