
from pymongo import MongoClient
from gridfs import GridFS
import os

url = 'mongodb+srv://'+{os.environ["USER_NAME"]}+':'+{os.environ['PASSWORD']}+'@blend.e8hq1yc.mongodb.net'; 
dbName = 'tracks'; 

def get_database():
    client = MongoClient(url)
    return client[dbName]
    
def get_bucket():
    bucket = GridFS(get_database(), collection='tracks')
    return bucket