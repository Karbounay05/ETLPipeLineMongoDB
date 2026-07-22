from pymongo import MongoClient
from config import *

client = MongoClient(MONGO_URI)

db = client[DATABASE_NAME]

def load_to_mongo(df, collection):

    db[collection].delete_many({})

    db[collection].insert_many(df.to_dict("records"))

    print(f"Loaded {len(df)} records into {collection}")