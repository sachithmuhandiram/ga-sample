from django.shortcuts import render
from django.http import HttpResponse
from databases.database_connection import DatabaseConnection


# Create your views here.
def index(request):
    # mongo_db_connection = DatabaseConnection.create_database_connection("MongoDB")

    # mongo_db = mongo_db_connection.connect_to_mongo_database()

    # mongo_db_collection = mongo_db["sample_course"]

    # otem = list(mongo_db_collection.find({"course_code": "ECX6236"}))
    # return HttpResponse(otem)

    return render(request, "user_module/login.html")
