from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from databases.database_connection import DatabaseConnection

mongo_db_connection = DatabaseConnection.create_database_connection("MongoDB")

mongo_db = mongo_db_connection.connect_to_mongo_database()

mongo_db_collection = mongo_db["sample_course"]


@api_view(["GET"])
def get_items(request):
    items = list(mongo_db_collection.find({"user_name": "sachith"}))
    for item in items:
        item["_id"] = str(item["_id"rest])
    return Response(items)


# Create your views here.
def index(request):
    # mongo_db_connection = DatabaseConnection.create_database_connection("MongoDB")

    # mongo_db = mongo_db_connection.connect_to_mongo_database()

    # mongo_db_collection = mongo_db["sample_course"]

    # otem = list(mongo_db_collection.find({"course_code": "ECX6236"}))
    # return HttpResponse(otem)

    return render(request, "user_module/login.html")
