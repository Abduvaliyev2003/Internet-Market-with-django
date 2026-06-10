from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render


from goods.models import Products


# Create your views here.
def catalog(request) -> HttpResponse:

    goods = Products.objects.all()
    context = {
        'title': 'Home - О нас  ',
        'goods': goods
    }
    return render(request, 'goods/catalog.html' , context)

def product(request) ->any:
    return render(request, 'goods/product.html')