from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.attractions, name='attractions'),
    path('<slug:slug>', views.single_attraction_page, name="single_activity_page")
]