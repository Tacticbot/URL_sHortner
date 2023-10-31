from fastapi import APIRouter, Depends, HTTPException, Header
from decouple import config
from model import *
from database import *


router = APIRouter()

URL_DICT = {}

@router.post('/', response_model= dict)
def post_url(url: LongUrlSchema):
    short_code = generate_short_url()

    # item_id = len(URL_DICT) + 1
    #[item_id]
    URL_DICT[short_code] = url.longurl
    return URL_DICT


