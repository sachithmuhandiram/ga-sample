from databases.database_connection import DatabaseConnection


class Main:

    def __init__(self) -> None:
        pass

    mongo_db_connection = DatabaseConnection.create_database_connection("MongoDB")

    mongo_db = mongo_db_connection.get_mongo_database()

    mongo_db_collection = mongo_db["sample_course"]

    print(list(mongo_db_collection.find({"course_code": "ECX6236"})))
