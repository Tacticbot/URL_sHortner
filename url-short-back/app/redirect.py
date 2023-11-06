from fastapi import APIRouter, Depends, HTTPException, Header
from starlette.responses import RedirectResponse
from model import *
from database import get_url_collection, get_database
from decouple import config

router = APIRouter()

@router.get("/{short_code}")
async def redirect_url(short_code : str):
    db =  get_database()
    collection = get_url_collection(db)

    url_data = await collection.find_one({"short_url": short_code})
    if not url_data:
        raise HTTPException(status_code= 401, detail="Short URL not found")

    return RedirectResponse(url= url_data["long_url"])