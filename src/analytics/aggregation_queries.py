from pymongo import MongoClient

from src.config import *

client = MongoClient(MONGO_URI)

db = client[DATABASE_NAME]

pipeline1 = [

    {
        "$count":"Total Users"
    }

]
pipeline2 = [

    {
        "$group":{

            "_id":"$department",

            "Average Salary":{"$avg":"$salary"}

        }

    }

]
pipeline3 = [

    {
        "$group":{

            "_id":"$product",

            "Total Revenue":{"$sum":"$price"}

        }

    }

]

pipeline4 = [
    {
        "$group": {
            "_id": "$city",
            "total_sales": {
                "$sum": "$price"
            }
        }
    }
]



pipeline5 = [
    {
        "$group": {
            "_id": "$department",
            "revenue": {
                "$sum": "$price"
            }
        }
    }
]


print("=== Total Documents ===")
print(list(db.sales.aggregate(pipeline1)))
print(list(db.employees.aggregate(pipeline1)))
print(list(db.users.aggregate(pipeline1)))
print("*******************************")
print("\n=== Average Salary by Department ===")
print(list(db.sales.aggregate(pipeline2)))
print(list(db.employees.aggregate(pipeline2)))
print(list(db.users.aggregate(pipeline2)))
print("*******************************")
print("\n=== Revenue by Product ===")
print(list(db.sales.aggregate(pipeline3)))
print(list(db.employees.aggregate(pipeline3)))
print(list(db.users.aggregate(pipeline3)))
print("*******************************")
print(list(db.warehouse.aggregate(pipeline4)))
print(list(db.warehouse.aggregate(pipeline5)))
