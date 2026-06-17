from django.shortcuts import render
from django.http import HttpResponse


def login(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home - Авторизация'
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
