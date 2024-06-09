from django.db import models

# Create your models here.

# Build a user module to store user information.
# Users can be academic_coordinator, course_coordinators, or administrators.
# Users can have multiple roles.
# Users can have multiple courses.
# User's information includes username, password, email, first name, last name, mobile_number and role are saved in the database.
# The user module should have a method to authenticate users.
# The user module should have a method to authorize users.
# The user module should have a method to add a new user.
# The user module should have a method to delete a user.
# The user module should have a method to update a user.
# The user module should have a method to get all users.
# Users can reset their password using forgotton password option.
# Users can update their profile.
# Users can view their profile.
# Users can change their password.
# Users can view their courses.
# Users can view their roles.
# Users can view their information.


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    # Create a function to authnticate users
    def authenticate_user(self, username, password):
        return self.username == username and self.password == password

    # Create a function to authorize users
    def authorize_user(self, role):
        return self.role == role

    # Create a function to add a new user
    def add_new_user(
        self,
        username,
        password,
        email,
        first_name,
        last_name,
        mobile_number,
        role,
        course,
    ):
        user = User(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            mobile_number=mobile_number,
            role=role,
            course=course,
        )
        user.save()

    # Create a function to delete a user
    def delete_user(self, username):
        user = User.objects.get(username=username)
        user.delete()

    # Create a function to update a user
    def update_user(
        self,
        username,
        password,
        email,
        first_name,
        last_name,
        mobile_number,
        role,
        course,
    ):
        user = User.objects.get(username=username)
        user.password = password
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.mobile_number = mobile_number
        user.role = role
        user.course = course
        user.save()

    # Create a function only administrator users can get all users details
    def get_all_users(self, role):
        if role == "administrator":
            return User.objects.all()
        else:
            return "You are not authorized to get all users details"

    # Create a function to reset password using forgotton password option
    def reset_password(self, email, new_password):
        user = User.objects.get(email=email)
        user.password = new_password
        user.save()

    # Create a function to update profile of own user
    def update_profile(
        self, username, email, first_name, last_name, mobile_number, course
    ):
        user = User.objects.get(username=username)
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.mobile_number = mobile_number
        user.course = course
        user.save()

    # Create a function to view profile of own user
    def view_profile(self, username):
        return User.objects.get(username=username)

    # Create a function to change password of own user
    def change_password(self, username, new_password):
        user = User.objects.get(username=username)
        user.password = new_password
        user.save()
