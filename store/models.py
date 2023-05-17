from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author = models.CharField(max_length=100, default='islam')

    def __str__(self):
        return f'{self.name}, {self.price}'
