from django.urls import path
from . import views

# from .views import get_items

app_name = "course_module"

urlpatterns = [
    path(
        "create_an_activity",
        views.create_an_activity,
        name="create_an_activity",
    ),
    path("save_an_activity", views.save_an_activity, name="save_an_activity"),
    path("define_a_course", views.define_a_course, name="define_a_course"),
    path(
        "save_course_meta_data",
        views.save_course_meta_data,
        name="save_course_meta_data",
    ),
    path(
        "define_course_activities_content",
        views.define_course_activities_content,
        name="define_course_activities_content",
    ),
]
