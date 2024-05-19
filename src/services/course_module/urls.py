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
]
