from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .serializers import BookSerializers
from store.models import Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        self.book_1 = Book.objects.create(name='test', price=25, author='zapa')
        self.book_2 = Book.objects.create(name='test1', price=125, author='islam')

    def test_get(self):
        url = reverse('book-list')
        response = self.client.get(url)
        serializers_data = BookSerializers([self.book_1, self.book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializers_data, response.data)

    def test_get_search(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'search': 'test'})
        serializers_data = BookSerializers([self.book_1, self.book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializers_data, response.data)

    def test_get_ordering(self):
        url = reverse('book-list')
        response = self.client.get(url, {'price__gte': 125.00})
        serializers_data = BookSerializers([self.book_1, self.book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializers_data, response.data)



