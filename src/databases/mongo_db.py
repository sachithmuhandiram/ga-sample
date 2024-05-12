class MongoDBConnection:

    def initialize_connection(self):
        print("Connecting to MongoDB")

    def insert_records(self, number_of_records):
        if number_of_records == "single":
            print("Just one mongo db record to DB")
        elif number_of_records == "multiple":
            print("Multiple records inserted to DB")
        else:
            raise ValueError("Not supported to insert")
