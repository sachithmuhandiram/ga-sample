from django.urls import path
from . import views
from .views import get_items

app_name = "user_module"

urlpatterns = [
    path("", views.index, name="index"),
    path("api/items/<str:username>/", get_items, name="get_items"),
]
