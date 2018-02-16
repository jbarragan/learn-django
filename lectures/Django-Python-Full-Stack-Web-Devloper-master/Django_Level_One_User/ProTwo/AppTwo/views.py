from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em>My Second Project</em>")

def help(request):
    context_dir = {"help_text": "This help is comming from Django!!"}
    return render(request, 'index.html', context=context_dir)
