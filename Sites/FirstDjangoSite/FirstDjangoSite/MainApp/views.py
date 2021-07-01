from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *


def first_view(request):
    cities = City.objects.all()
    print(cities)
    return HttpResponse('<p>Ну привет)</p>')

