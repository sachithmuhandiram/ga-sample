import configparser
from pymongo import MongoClient


class MongoDBConnection:

    def __init__(self) -> None:
        config = configparser.ConfigParser()

        config.read("config/config.ini")
        self.connection_url = config.get("Mongo", "url")
        self.database = "sample_db"  # config.get("Mongo", "database")

    def get_mongo_database(self):
        mongo_db_conn = MongoClient(self.connection_url)
        mongo_db = mongo_db_conn[self.database]
        return mongo_db

    def insert_records(self, number_of_records):
        if number_of_records == "single":
            print("Just one mongo db record to DB")
        elif number_of_records == "multiple":
            print("Multiple records inserted to DB")
        else:
            raise ValueError("Not supported to insert")
