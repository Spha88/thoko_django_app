from django.shortcuts import render

def home(request):
    return render(request, 'pages/index.html')

def activities(request):
    return render(request, 'pages/activities.html')