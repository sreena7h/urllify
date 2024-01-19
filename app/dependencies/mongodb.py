from pymongo import MongoClient
from app.settings import DATABASE_HOST, DATABASE_AGENT, DATABASE_PORT, \
    DATABASE_NAME


def get_database():
    database_url = f"{DATABASE_AGENT}://{DATABASE_HOST}:{DATABASE_PORT}"
    client = MongoClient(database_url)
    db = client[DATABASE_NAME]
    return db
