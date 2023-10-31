from fastapi import FastAPI, HTTPException, Depends, status, Request
from fastapi.responses import JSONResponse, HTMLResponse
from shortener import router as ShortRouter
from redirect import router as RedirectRouter

from contextlib import asynccontextmanager
from database import *


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db()
    yield
    await shutdown_db()
    

app = FastAPI(lifespan=lifespan)

app.include_router(ShortRouter, tags=["Test"], prefix = "/api/shorten")

app.include_router(RedirectRouter, tags = ["Redirect to Short URL"])


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


