from fastapi import APIRouter, HTTPException,  Request
from decouple import config
from model import *
from database import get_database, get_url_collection


router = APIRouter()


@router.post('/', response_model= UrlSchema)
async def post_url(payload: LongUrl, request: Request):
    short_code = generate_short_url()
    created_at = datetime.now().isoformat()
    base_url = request.base_url

    db = get_database()
    collection = get_url_collection(db)

    check = await collection.find_one({"short_url": short_code})
    if check:
        raise HTTPException(status_code = 400, detail = "Short code is invalid, It has been used.")

    await collection.insert_one({"short_url": short_code, "long_url": str(payload.long_url), "created_at": created_at})
    
    return UrlSchema(short_url=f"{base_url}{short_code}", long_url=payload.long_url, created_at=created_at)

