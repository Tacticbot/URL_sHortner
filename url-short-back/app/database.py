import motor.motor_asyncio
from decouple import config


uri = config("MONGO_STRING")

mongo_client = motor.motor_asyncio.AsyncIOMotorClient(uri)

try:
    res = mongo_client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

def get_database():
    db = mongo_client["url_store"]
    return db

def get_url_collection(db):
    return db["url_collection"]

def shutdown_db():
    mongo_client.close()
