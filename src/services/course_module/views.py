from django.shortcuts import render


def create_an_activity(request):
    return render(request, "course_module/create_an_activity.html")
