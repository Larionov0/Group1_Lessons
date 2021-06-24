from django.urls import path, include
from .views import first_view


urlpatterns = [
    path('first/', first_view),
]
