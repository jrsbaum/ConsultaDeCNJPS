from pymongo import MongoClient
from cfg import mongo_client_key


class Db:
    def insert_to_db(self, data):
        try:
            client = MongoClient(mongo_client_key)
            db = client.CNPJS
            cnpjs = db.cnpjs
            cnpjs.insert_one(data)
        except Exception as e:
            print(f"An error occurred while trying to insert the data in MongoDB: {e}")


