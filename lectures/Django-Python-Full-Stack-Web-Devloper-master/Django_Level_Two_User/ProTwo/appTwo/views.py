from django.shortcuts import render
from appTwo.models import User

def index(request):
    return render(request, "appTwo/index.html")

def users(request):
    users_list = User.objects.order_by("first_name")
    users_dict = {"users": users_list}
    return render(request, "appTwo/users.html", context=users_dict)
