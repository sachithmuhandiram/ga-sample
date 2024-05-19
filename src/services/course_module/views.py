from django.shortcuts import render
from django.shortcuts import render
from .models import CourseActivity
from django import forms


class CreateNewActivity(forms.Form):
    activity_name = forms.CharField(label="New Activity", max_length=100)
    has_groups = forms.BooleanField(label="Has Groups", required=False)


def create_an_activity(request):
    return render(request, "course_module/create_an_activity.html")


def save_an_activity(request):
    if request.method == "POST":

        # Get the new activity from the form
        new_activity = CreateNewActivity(request.POST)

        if new_activity.is_valid():
            # Save the new activity to the database
            activity = CourseActivity(
                activity_name=new_activity.cleaned_data["activity_name"],
                has_groups=new_activity.cleaned_data["has_groups"],
            )
            print(new_activity.cleaned_data["activity_name"])
            activity.save()

            # Redirect to a success page

        return render(request, "course_module/create_an_activity.html")
    else:
        # Handle other request methods (e.g., GET)
        print("Something not right")
        return render(request, "course_module/create_an_activity.html")
