from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from users.forms import UserLoginForm

def login(request) -> HttpResponse:
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        from = UserLoginForm()
    context: dict[str, str] = {
        'title': 'Home - Авторизация'
        'form': from,
    }

    return render(request, 'users/login.html', context)


def registration(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home - Регистрация'
    }

    return render(request, 'users/registration.html', context)


def profile(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home - Кабинет'
    }

    return render(request, 'users/profile.html', context)


def logout(request):
    pass
