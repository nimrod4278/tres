import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = os.environ.get("MONGO_CONNECTION_STRING")


class MongoClient():
    def __init__(self) -> None:
        self.client = pymongo.MongoClient(CONNECTION_STRING)
    
    def get_db(self, db_name):
        db = {}
        try:
            db = self.client[db_name]
        except Exception as e:
            print(f"[ERROR] - MONGO - get_db - {db_name}")
            print(e)
        return db
    
    def get_collection(self, db_name, collection_name):
        collection = {}
        try:
            collection = self.client[db_name][collection_name]
        except Exception as e:
            print(f"[ERROR] - MONGO - get_collection - {db_name} - {collection_name}")
            print(e)
        return collection
    
    def insert_many(self, db_name, collection_name, docs):
        insert_result = {}
        try:
            insert_result = self.client[db_name][collection_name].insert_many(docs)
        except Exception as e:
            print(f"[ERROR] - MONGO - insert_many - {db_name} - {collection_name}")
            print(docs)
            print(e)
    
    def insert_one(self, db_name, collection_name, doc):
        insert_result = {}
        try:
            insert_result = self.client[db_name][collection_name].insert_one(doc) 
        except Exception as e:
            print(f"[ERROR] - MONGO - insert_one - {db_name} - {collection_name}")
            print(doc)
            print(e)
        
        return insert_result 

    def find(self, db_name, collection_name, query, options={}):
        return self.client[db_name][collection_name].find(query, options)
    
    def find_one(self, db_name, collection_name, filter):
        return self.client[db_name][collection_name].find_one(filter)