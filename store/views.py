import django_filters
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from store.models import Book
from store.serializers import BookSerializers


class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['price']
    search_fields = ['name', 'author']
    ordering_fields = ['author', 'price']


def auth(request):
    return render(request, 'oauth.html')

