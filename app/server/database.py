from pymongo import  MongoClient
from pymongo.server_api import ServerApi


uri = 'mongodb+srv://imusa4918:PpmoPhourizZiyDr@cluster0.trkisj2.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["urlstore"]


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)