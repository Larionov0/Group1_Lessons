from django.urls import path, include
from .views import *


urlpatterns = [
    path('first/', first_view),
    path('all_cities/', show_cities),
    path('all_reviews/', all_reviews)
]
