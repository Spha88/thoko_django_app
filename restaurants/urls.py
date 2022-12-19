from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.restaurants, name='dining'),
    path('<slug:slug>', views.restaurant_single_page, name="dining_single_page")
]