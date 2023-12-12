from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5,decimal_places=0)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images')


    def __str__(self):
        return self.name

    def __str__(self):
        return f'Книга: {self.name}'




