from fastapi import FastAPI
from pymongo import  MongoClient
from pymongo.server_api import ServerApi
import motor.motor_asyncio
from decouple import config


uri = config("MONGO_STRING")

client = motor.motor_asyncio.AsyncIOMotorClient(uri)
db = client.urls

try:
    res = client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)