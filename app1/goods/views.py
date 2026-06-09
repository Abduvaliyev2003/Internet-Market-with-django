from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def catalog(request) -> HttpResponse:
    context: dict[str, any] = {
        'title': 'Home - О нас  ',
        'goods': [
            {'image': 'deps/images/goods/set of tea table and three chairs.jpg',
             'name': 'Чайный столик и три стула',
             'description': 'Комплект из трёх стульев и дизайнерский столик для гостинной комнаты.',
             'price': 150.00},

            {'image': 'deps/images/goods/set of tea table and three chairs.jpg',
             'name': 'Чайный столик и три стула',
             'description': 'Комплект из трёх стульев и дизайнерский столик для гостинной комнаты.',
             'price': 150.00},
       ]
    }
    return render(request, 'goods/catalog.html' , context)

def product(request) ->any:
    return render(request, 'goods/product.html')