from dotenv import load_dotenv
from pymongo import MongoClient
from utils import *
import os

load_dotenv()

# connect to DBs

oldDb = MongoClient(os.getenv('MONGO_OLD_URI'))[os.getenv('MONGO_OLD_DB')]
newDb = MongoClient(os.getenv('MONGO_NEW_URI'))[os.getenv('MONGO_NEW_DB')]

# TODO: make these env variables??

creation_opts = {
    'solution_paths': { 'storageEngine': { 'wiredTiger': { 'configString': 'block_compressor=zstd', } } },
    'instances': {},
    'submissions': {},
}

stream_opts = {
    'solution_path': lambda x: encodeRLE(mathOriginToPixelOrigin(x)),
}

for collection_name in os.getenv('MONGO_LARGE_COLLECTIONS').split(":"):
    newDb.create_collection(collection_name, **creation_opts[collection_name])
    streamDocs(oldDb[collection_name], newDb[collection_name]) #**stream_opts)
