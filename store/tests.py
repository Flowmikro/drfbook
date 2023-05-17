from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .serializers import BookSerializers
from store.models import Book


class BookAPITestCase(APITestCase):
    def test_get(self):
        book_1 = Book.objects.create(name='test', price=25)
        book_2 = Book.objects.create(name='test1', price=125)
        url = reverse('book-list')
        response = self.client.get(url)
        serializers_data = BookSerializers([book_1, book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializers_data, response.data)

