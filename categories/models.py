from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Categories')
    image = models.ImageField(upload_to='categories/', null=True)

    def __str__(self):
        return self.name