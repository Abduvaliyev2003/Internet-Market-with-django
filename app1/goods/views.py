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

def product(request, product_slug =False, product_id= False) ->any:
    if product_id:
        product = Products.objects.get(id=product_id)
    else:
        product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }

    return render(request, 'goods/product.html', context=context)