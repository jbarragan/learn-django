from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = { 'insert_me': "Hello I am from views.py and my template is comming from first_app/index.html !!" }
    return render(request, 'first_app/index.html', context=my_dict)

def picture(request):
    return render(request, 'first_app/picture.html', context={})
