from django.shortcuts import render
from .models import Restaurant
from .helper_functions import add_num_of_star_list

def restaurants(request):
    restaurants = Restaurant.objects.all()
    restaurants = add_num_of_star_list(restaurants)
    return render(request, 'pages/restaurants.html', { 'restaurants': restaurants})

def restaurant_single_page(request, slug):
    restaurant = Restaurant.objects.get(slug=slug)
    return render(request, 'pages/single_restaurant_page.html', {'restaurant': restaurant})
