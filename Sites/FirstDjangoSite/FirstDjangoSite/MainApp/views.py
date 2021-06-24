from django.shortcuts import render
from django.shortcuts import HttpResponse


def first_view(request):
    return HttpResponse('<p>Ну привет)</p>')

