from fastapi import FastAPI
import motor.motor_asyncio
from decouple import config


uri = config("MONGO_STRING")

mongo_client = motor.motor_asyncio.AsyncIOMotorClient(uri)

try:
    res = mongo_client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

async def create_db():
    uri = config("MONGO_STRING")

    mongo_client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    db = mongo_client["urlstore"]


async def get_db():
    uri = config("MONGO_STRING")

    mongo_client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    db = mongo_client["urlstore"]
    collection = db["url_collection"]
    return collection
    
    

async def shutdown_db():
    mongo_client.close()

