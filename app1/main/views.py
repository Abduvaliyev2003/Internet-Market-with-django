from http.client import HTTPResponse
from multiprocessing import context

from django.db.models.fields import return_None
from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories
# Create your views here.

def index(request) -> HttpResponse:

    categories = Categories.objects.all()

    context: [str, str] = {
        'title': 'Home',
        'content': 'Главная странница магазина - Home',
        'categories': categories,
    }
    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context: [str, str] = {
        'title': 'Home - О нас  ',
        'content': ' О нас ',
        'text_on_page': 'Иван поступил правильно, когда открылся мальчику и помог ему с учебой.'
    }
    return render(request, 'main/about.html', context)


