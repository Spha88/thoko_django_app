from django.shortcuts import render
from .models import Attraction

def attractions(request):
    attractions = Attraction.objects.all().order_by('title')

    edited_attractions = []
    for attraction in attractions:
        attraction.num_of_stars = [] #adding a new field in attraction
        for _ in range(attraction.stars):
            attraction.num_of_stars.append('star')
        edited_attractions.append(attraction)
    
    return render(request, 'pages/attractions.html', { 'attractions': edited_attractions })

def single_attraction_page(request, slug):
    attraction = Attraction.objects.get(slug=slug)
    return render(request, 'pages/single_attraction_page.html', {'attraction': attraction})