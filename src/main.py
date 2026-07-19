from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME

try:
    client = MongoClient(MONGO_URI)

    # Test the connection
    client.admin.command("ping")

    print("✅ Connected to MongoDB!")

    db = client[DATABASE_NAME]

    print(f"Database: {DATABASE_NAME}")
    print("Collections:", db.list_collection_names())

except Exception as e:
    print("❌ Connection failed")
    print(e)