from django.shortcuts import render

def index(request):
    context_dict = {"subtitle": "Subtitle from FirstApp index view"}
    return render(request, 'first_app/index.html', context=context_dict)
