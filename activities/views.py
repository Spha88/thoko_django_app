from django.shortcuts import render
from .models import Activity

def activities(request):
    activities = Activity.objects.all()
    return render(request, 'pages/activities.html', { 'activities': activities })

def single_activity_page(request, slug):
    activity = Activity.objects.get(slug=slug)
    return render(request, 'pages/single_activity_page.html', {'activity': activity})
