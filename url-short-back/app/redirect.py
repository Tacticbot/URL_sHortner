from fastapi import APIRouter, Depends, HTTPException, Header
from starlette.responses import RedirectResponse
from model import *
from shortener import URL_DICT
from decouple import config

router = APIRouter()

@router.get("/{short_code}")
async def redirect_url(short_code : str):
    # collection = database.get_collection("urls")
    # url_item = await collection.find_one({"short_url": short_url})
    url_item = URL_DICT[short_code]
    
    if url_item:
        return RedirectResponse(URL_DICT[short_code])
    else:
        raise HTTPException(status_code=404, detail="Short URL not found")