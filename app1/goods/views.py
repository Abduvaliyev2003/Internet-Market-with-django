from http.client import HTTPResponse

from django.core import paginator
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from goods.models import Products


# Create your views here.
def catalog(request, category_slug=None, page=1):
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(
            category__slug=category_slug
        )
    paginator = Paginator(goods, 3)
    page = request.GET.get('page', 1)
    current_page = paginator.get_page(page)

    context = {
        'title': 'Home - О нас',
        'goods': current_page,
        'slug_url': category_slug,
    }

    return render(request, 'goods/catalog.html', context)

def product(request, product_slug =False, product_id= False) ->any:
    if product_id:
        product = Products.objects.get(id=product_id)
    else:
        product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }

    return render(request, 'goods/product.html', context=context)