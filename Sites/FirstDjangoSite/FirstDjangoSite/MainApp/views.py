from django.shortcuts import render, redirect
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
    user = request.user
    revs = Review.objects.all()
    return render(request, 'all_reviews.html', context={'reviews': revs, 'user': user, 'is_auth': user.is_authenticated})


def edit_review(request, rev_id):
    review = Review.objects.get(id=rev_id)

    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        name = request.POST['name']
        text = request.POST['text']
        rate = request.POST['rate']
        shop_id = request.POST['shop']
        shop = Shop.objects.get(id=shop_id)

        review.name = name
        review.text = text
        review.rate = rate
        review.shop = shop

        review.save()

    return render(request, 'edit_review.html', context={'review': review, 'shops_list': Shop.objects.all()})


def create_review(request):
    new_review = Review.objects.create(
        name='Новый обзор',
        text='',
        shop=Shop.objects.all()[0],
    )
    return redirect(f'/main/edit_review/{new_review.id}')


def delete_review(request, rev_id):
    Review.objects.get(id=rev_id).delete()
    return redirect('/main/all_reviews')
