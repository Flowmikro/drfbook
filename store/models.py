from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author = models.CharField(max_length=100, default='islam')

    def __str__(self):
        return f'{self.name}, {self.price}'


class UserBookRelation(models.Model):
    RATE_CHOICES = (
        (1, 'Очень плохо'),
        (2, 'Плохо'),
        (3, 'Нормально'),
        (4, 'Хорошо'),
        (5, 'Очень хорошо'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return f'{self.user}, {self.book}'
