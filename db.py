"""
    db.py file contains MongoDB client which can be used to connect and query the Database.
"""
from pymongo import MongoClient
from app_settings import (MONGODB_HOST, MONGODB_NAME, MONGODB_PASSWORD, MONGODB_USERNAME)


mongo_uri = "mongodb+srv://{username}:{password}@{host}/{db_name}".format(
    username=MONGODB_USERNAME, password=MONGODB_PASSWORD, host=MONGODB_HOST, db_name=MONGODB_NAME)

client = MongoClient(mongo_uri)
database = client[MONGODB_NAME]
collection = 'heruken'
