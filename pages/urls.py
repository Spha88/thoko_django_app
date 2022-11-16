from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('activities', views.activities, name='activities')
]