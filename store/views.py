from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from store.models import Book
from store.serializers import BookSerializers


class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

