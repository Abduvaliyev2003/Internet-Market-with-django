from django.db import models

from goods.models import Products
from users.models import User


class Cart(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='User',
    )
    product = models.ForeignKey(
        to=Products,
        on_delete=models.CASCADE,
        verbose_name='Product',
    )
    quantity = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Quantity',
    )
    session_key = models.CharField(
        max_length=32,
        null=True,
        blank=True,
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created',
    )

    class Meta:
        db_table = 'cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f'Cart {self.user} | Product {self.product.name} | Qty {self.quantity}'
