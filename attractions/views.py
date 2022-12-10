from django.shortcuts import render
from .models import Attraction

def attractions(request):
    attractions = Attraction.objects.all()
    return render(request, 'pages/attractions.html', { 'attractions': attractions })

def single_attraction_page(request, slug):
    attraction = Attraction.objects.get(slug=slug)
    return render(request, 'pages/single_attraction_page.html', {'attraction': attraction})