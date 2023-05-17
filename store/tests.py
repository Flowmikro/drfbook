import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .serializers import BookSerializers
from store.models import Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_username')
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

    def test_post(self):
        self.assertEqual(2, Book.objects.all().count())
        url = reverse('book-list')
        data = {
            "name": "test для начинающих",
            "price": 1899.00,
            "author": "test islam"
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, Book.objects.all().count())

    def test_put(self):
        url = reverse('book-detail', args=(self.book_1.id,))
        data = {
            "name": self.book_1.name,
            "price": 1899.00,
            "author": self.book_1.author
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.book_1.refresh_from_db()
        self.assertEqual(1899.00, self.book_1.price)

    def test_delete(self):
        self.assertEqual(2, Book.objects.all().count())
        url = reverse('book-detail', args=(self.book_1.id,))
        data = {
            "name": self.book_1.name,
            "price": 1899.00,
            "author": self.book_1.author
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.delete(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(1, Book.objects.all().count())

