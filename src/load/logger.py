from pymongo import MongoClient
from datetime import datetime

from config import  *

client = MongoClient(MONGO_URI)

db = client[DATABASE_NAME]


def log_pipeline(status, records, message=""):

    db[LOG_COLLECTION].insert_one({

        "time": datetime.now(),

        "status": status,

        "records_processed": records,

        "message": message

    })