from django.urls import path
from . import views

app_name = "user_module"

urlpatterns = [
    path("", views.login, name="login"),
    path("authenticate_user", views.authenticate_user, name="authenticate_user"),
    path("authorize_user", views.authorize_user, name="authorize_user"),
    path("register", views.register, name="register"),
    path("register_user", views.register_user, name="register_user"),
]
