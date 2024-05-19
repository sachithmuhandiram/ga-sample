from django.shortcuts import render
from django.shortcuts import render
from .models import CourseActivity
from django import forms


class CreateNewActivity(forms.Form):
    activity = forms.CharField(label="New Activity", max_length=100)
    has_groups = forms.BooleanField(label="Has Groups", required=False)


def create_an_activity(request):
    return render(request, "course_module/create_an_activity.html")


def save_an_activity(request):
    if request.method == "POST":

        # Get the new activity from the form
        new_activity = request.POST.get("new_activity")
        has_groups = request.POST.get("has_groups")

        # Save the new activity to the database
        activity = CourseActivity(activity_name=new_activity, has_groups=has_groups)
        # should be with pymongo

        return render(request, "course_module/create_an_activity.html")
    else:
        # Handle other request methods (e.g., GET)
        print("Something not right")
        return render(request, "course_module/create_an_activity.html")
