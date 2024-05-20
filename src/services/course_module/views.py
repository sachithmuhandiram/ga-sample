from django.shortcuts import render
from django.shortcuts import render
from .models import CourseActivity
from django import forms
from databases.database_connection import DatabaseConnection
import json

mongo_db_connection = DatabaseConnection.create_database_connection("MongoDB")

mongo_db = mongo_db_connection.connect_to_mongo_database()


class CreateNewActivity(forms.Form):
    activity = forms.CharField(label="New Activity", max_length=100)
    has_groups = forms.BooleanField(label="Has Groups", required=False)


def create_an_activity(request):
    return render(request, "course_module/create_an_activity.html")


def save_an_activity(request):
    if request.method == "POST":
        mongo_db_collection = mongo_db["course_activities"]
        # Get the new activity from the form
        new_activity = request.POST.get("new_activity")
        has_groups = request.POST.get("has_groups")

        # Create a python dictionary named course_data
        activity_data = {"activity_name": new_activity, "has_groups": has_groups}

        mongo_db_collection.insert_one(activity_data)

        return render(request, "course_module/create_an_activity.html")
    else:
        # Handle other request methods (e.g., GET)
        print("Something not right")
        return render(request, "course_module/create_an_activity.html")
