from django import template
from goods.models import Categories


register = template.Library()

def tag_catergories():
    return Categories.objects.all()