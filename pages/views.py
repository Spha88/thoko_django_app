from django.shortcuts import render

from activities.models import Activity

def home(request):
    return render(request, 'pages/index.html')