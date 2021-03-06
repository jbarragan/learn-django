from django.shortcuts import render
from first_app.models import Topic, Webpage, AccessRecord, User

def index(request):
    context_dict = {"subtitle": "Subtitle from FirstApp index view"}
    return render(request, 'first_app/index.html', context=context_dict)

def webpages(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = { 'access_records': webpage_list }
    return render(request, 'first_app/webpages.html', context=date_dict)

def users(request):
    users_list = User.objects.order_by('first_name')
    users_dict = { 'user_records': users_list }
    return render(request, 'first_app/users.html', context=users_dict)
