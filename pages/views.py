from django.shortcuts import render

from restaurants.models import Restaurant
from thoko_website.helper_functions import make_extract

def home(request):
    restaurants = Restaurant.objects.all()[:3]

    for restaurant in restaurants:
        restaurant.extract = make_extract(restaurant.owner_description, 20)

    context = {
        'restaurants' : restaurants,
    }

    return render(request, 'pages/index.html', context )