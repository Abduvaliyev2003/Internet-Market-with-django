from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='name')
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True, verbose_name='URl')

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='name')
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True, verbose_name='URl')
    description = models.TextField(blank=True, null=True, verbose_name='description')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='image')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2,  verbose_name='price')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='discount')
    quantity = models.PositiveIntegerField(default=0, verbose_name='quantity')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='category')
    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
