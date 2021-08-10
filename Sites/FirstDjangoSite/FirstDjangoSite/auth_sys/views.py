from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout


def sign_up(request):
    pass


def sign_in(request):
    print(request.method)
    print(request.GET)
    print(request.POST)

    if request.method == 'GET':
        return render(request, 'sign_in.html')
    elif request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/main/all_reviews')
        else:
            print('Auth wrong')
            return render(request, 'sign_in.html', context={'error': 'Такого пользователя у нас нету :('})


def logout(request):
    pass
