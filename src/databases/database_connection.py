from .mongo_db import MongoDBConnection
from .mysql_db import MySQLDBConnection


class DatabaseConnection:
    @staticmethod
    def create_database_connection(database_type):
        if database_type == "MySQL":
            return MySQLDBConnection()
        elif database_type == "MongoDB":
            return MongoDBConnection()
        else:
            raise ValueError("Un supported DB type")
