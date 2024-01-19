from pymongo import ASCENDING

from app.dependencies.mongodb import get_database

database = get_database()

collection = database["UsedIdentifiers"]
collection.create_index([("uuid", ASCENDING)], unique=True)
