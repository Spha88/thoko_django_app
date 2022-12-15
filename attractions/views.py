from django.shortcuts import render
from .models import Attraction

# Helper function
def add_num_of_star_list(attractions):
    '''
        Add number_of_stars list to each attraction based on the "stars" field to be looped in template
    '''
    
    edited_attractions = []
    for attraction in attractions:
        attraction.num_of_stars = [] #adding a new field in attraction
        for _ in range(attraction.stars):
            attraction.num_of_stars.append('star')
        edited_attractions.append(attraction)
    return edited_attractions


def attractions(request):
    attractions = Attraction.objects.all().order_by('title')
    attractions = add_num_of_star_list(attractions)
    
    return render(request, 'pages/attractions.html', { 'attractions': attractions })

def single_attraction_page(request, slug):
    attraction = Attraction.objects.get(slug=slug)
    attractions = Attraction.objects.all().order_by('title').exclude(slug=slug)[:8]
    attractions = add_num_of_star_list(attractions)

    payload = {
        'attraction': attraction, 
        'attractions': attractions 
    }

    return render(request, 'pages/single_attraction_page.html', payload)