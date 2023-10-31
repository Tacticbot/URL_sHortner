from datetime import datetime 
import string
import random
from pydantic import BaseModel, HttpUrl
from pydantic_core import Url


class UrlSchema(BaseModel):
    short_url: str
    created_at: str
    

    class Config:
        schema_extra = {
            "example": {
                "short_url": "https://try23g.co",
                "created_at": "12:00:423"

            }
        }
class LongUrlSchema(BaseModel):
    longurl: HttpUrl

    class Config:
        schema_extra = {
            "example": {
                "longurl": "https://www.google.com/?user=FTBBhwkjdggh8478930764553"
            }
        }

url_dict = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))


def generate_and_store_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))


    created_at = datetime.now().isoformat()
    
    url_item = UrlSchema(short_url=short_url, created_at=created_at)
    return 

print(generate_and_store_short_url())
print(url_dict)