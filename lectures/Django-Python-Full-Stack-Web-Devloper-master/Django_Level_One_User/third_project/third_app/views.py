from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    my_dict = { 'insert_me': "Hello" }
    return render(request, 'home.html', context=my_dict)

def help(request):
    context_dir = {"help_text": "This help is comming from Django!!"}
    return render(request, 'third_app/help.html', context=context_dir)
