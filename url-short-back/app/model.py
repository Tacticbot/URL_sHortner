from datetime import datetime 
import string
import random
from pydantic import BaseModel, HttpUrl





class UrlSchema(BaseModel):
    short_url: str
    long_url: HttpUrl
    created_at: str

    class Config:
        schema_extra = {
            "example": {
                "short_url": "https://short.ly/abc123",
                "long_url": "https://www.example.com",
                "created_at": "2023-11-03T12:00:42.300Z"
            }
        }

class LongUrl(BaseModel):
    long_url: HttpUrl

    
def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))


