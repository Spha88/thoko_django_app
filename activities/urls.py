from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.activities, name='activities'),
    path('<slug:slug>', views.single_activity_page, name="single_activity_page")
]
