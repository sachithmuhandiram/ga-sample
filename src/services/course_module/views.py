from django.shortcuts import render
from django.shortcuts import render
from .models import CourseActivity
from django import forms


class CreateNewActivity:
    new_activity = forms.CharField(label="New Activity", max_length=100)
    has_groups = forms.BooleanField(label="Has Groups", required=False)


def create_an_activity(request):
    return render(request, "course_module/create_an_activity.html")


def post_an_activity(request):
    if request.method == "POST":

        # Get the new activity from the form
        new_activity = CreateNewActivity(request.POST)

        if new_activity.is_valid():
            # Save the new activity to the database
            activity = CourseActivity(
                activity_name=new_activity.cleaned_data["new_activity"],
                has_groups=new_activity.cleaned_data["has_groups"],
            )
            activity.save()

            # Redirect to a success page

        return render(request, "course_module/success.html")
    else:
        # Handle other request methods (e.g., GET)
        return render(request, "course_module/create_an_activity.html")
