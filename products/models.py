from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

from categories.models import Category

# Create your models here.
class Banner(models.Model):
    img = models.ImageField(upload_to='banners/')

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    in_stock = models.IntegerField(default=0)
    expire_date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(Category,related_name='products', on_delete=models.CASCADE, null='True')

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

    def __str__(self) -> str:
        return self.product.name