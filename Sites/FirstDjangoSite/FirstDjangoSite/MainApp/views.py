from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *


def first_view(request):
    cities = City.objects.all()
    ul = '<ul>'
    for city in cities:
        ul += f'<li>{city.name}</li>'
    ul += '</ul>'
    return HttpResponse('<p>Ну привет)</p>' + ul)


def show_cities(request):
    cities = City.objects.all()
    return render(request, 'show_cities.html',
                  context={
                      'a': 'Привет из контекста!',
                      'cities': cities
                  })


def all_reviews(request):
    revs = Review.objects.all()
    return render(request, 'all_reviews.html', context={'reviews': revs})

