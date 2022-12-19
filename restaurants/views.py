from django.shortcuts import render
from .models import Restaurant

def restaurants(request):
    return render(request, 'pages/restaurants.html')

def restaurant_single_page(request):
    return render(request, 'pages/single_restaurant_page.html')
