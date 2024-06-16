from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from django import forms
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from bson import json_util


# View for login page
def login(request):
    return render(request, "user_module/login.html")


# view for user authentication
@api_view(["POST"])
def authenticate_user(request):

    if request.method == "POST":
        try:
            username = request.data["username"]
            password = request.data["password"]
            user = User.objects.get(username=username)
            if user.authenticate_user(username, password):
                return JsonResponse(
                    {"message": "User  authenticated", "status": 200},
                    content_type="application/json",
                )
            else:
                return JsonResponse(
                    {"message": "User not authenticated", "status": 401},
                    content_type="application/json",
                )
        except User.DoesNotExist:
            # log to file regarding user module
            return JsonResponse(
                {"message": "User not authenticated", "status": 400},
                content_type="application/json",
            )


# view for user authorization
@api_view(["POST"])
def authorize_user(request):
    if request.method == "POST":
        username = request.data["username"]
        role = request.data["role"]
        user = User.objects.get(username=username)
        if user.authorize_user(role):
            return Response({"message": "User authorized"})
        else:
            return Response({"message": "User not authorized"})


# view for user registration page
def register(request):
    return render(request, "user_module/register.html")


# view for user registration
@api_view(["POST"])
def register_user(request):
    if request.method == "POST":
        print(request.data)
        username = request.data["username"]
        password = request.data["password"]
        email = request.data["email"]
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]
        mobile_number = request.data["mobile_number"]
        user = User()
        user.add_new_user(
            username,
            password,
            email,
            first_name,
            last_name,
            mobile_number,
        )
        return Response({"message": "User registered"})
