from django.shortcuts import render
from django.shortcuts import render
from .models import CourseActivity
from django import forms
from databases.database_connection import DatabaseConnection
import json

mongo_db_connection = DatabaseConnection.create_database_connection("MongoDB")

mongo_db = mongo_db_connection.connect_to_mongo_database()
mongo_course_activity_collection = mongo_db["course_activities"]


class CreateNewActivity(forms.Form):
    activity = forms.CharField(label="New Activity", max_length=100)
    has_groups = forms.BooleanField(label="Has Groups", required=False)


def create_an_activity(request):
    return render(request, "course_module/create_an_activity.html")


def define_a_course(request):
    # Get data from mongo db about the all course activities
    course_activities = mongo_course_activity_collection.find({})

    return render(
        request,
        "course_module/define_a_course.html",
        {"course_activities": course_activities},
    )


def save_course_meta_data(request):

    if request.method == "POST":
        course_code = request.POST.get("courseCode")
        course_activities = request.POST.getlist("activities")

        print("Course code : ", course_code)
        print("Course has : ", course_activities)

        mongo_course_meta_data = mongo_db["course_meta_data"]

        course_meta_data = {
            "course_code": course_code,
            "course_activities": course_activities,
        }
        mongo_course_meta_data.insert_one(course_meta_data)
        return define_a_course(request)


def save_an_activity(request):
    if request.method == "POST":

        # Get the new activity from the form
        new_activity = request.POST.get("new_activity")
        has_groups = request.POST.get("has_groups")

        if has_groups == "on":
            has_groups = True
        else:
            has_groups = False

        # Create a python dictionary named course_data
        activity_data = {"activity_name": new_activity, "has_groups": has_groups}

        mongo_course_activity_collection.insert_one(activity_data)

        return render(request, "course_module/create_an_activity.html")
    else:
        # Handle other request methods (e.g., GET)
        print("Something not right")
        return render(request, "course_module/create_an_activity.html")
