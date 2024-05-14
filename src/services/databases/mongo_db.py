import configparser
from pymongo import MongoClient
import os.path


class MongoDBConnection:

    def __init__(self) -> None:
        config = configparser.ConfigParser()
        current_path = os.path.dirname(__file__)
        config_file = os.path.join(current_path, "config", "config.ini")

        config.read(config_file)
        self.connection_url = config.get("Mongo", "url")
        self.database = config.get("Mongo", "database")

    def connect_to_mongo_database(self):
        print(self.connection_url)
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
