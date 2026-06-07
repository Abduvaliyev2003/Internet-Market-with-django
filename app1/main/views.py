from http.client import HTTPResponse
from multiprocessing import context

from django.db.models.fields import return_None
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request) -> HttpResponse:
    context: [str, str] = {
        'title': 'Home',
        'content': 'Главная странница магазина - Home'
    }
    return render(request, 'main/index.html', context)
