from django.db import models

from categories.models import Category

# Create your models here.
class Banner(models.Model):
    img = models.ImageField(upload_to='banners/')



class Product(models.Model):
    title = models.CharField(max_length= 200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places= 2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(Category,related_name='products', on_delete=models.CASCADE, null='True')

    def __str__(self):
        return self.title

