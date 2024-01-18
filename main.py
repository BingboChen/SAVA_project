
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
from icecream import ic

load_dotenv()
username = os.getenv('MONGODB_USERNAME')
password = os.getenv('MONGODB_PASSWORD')

uri = f"mongodb+srv://{username}:{password}@cluster0.m7203dx.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)





