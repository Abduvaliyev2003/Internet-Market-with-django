from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories


def index(request) -> HttpResponse:
    context = {
        'title': 'Home',
        'content': 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Мы — команда профессионалов, которая помогает создать уютный дом. '
                        'Наш магазин предлагает широкий ассортимент качественной мебели '
                        'для кухни, спальни, гостиной и офиса по доступным ценам.'
    }
    return render(request, 'main/about.html', context)
