from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Tags


class TagsTests(APITestCase):
    def setUp(self):
        self.page_counts = {"html": 1,
                            "head": 1,
                            "title": 1,
                            "link": 9,
                            "meta": 19,
                            "script": 12}

        self.not_null_tags_counter = Tags.objects.create(
            tag_counter=self.page_counts)
        self.null_tags_counter = Tags.objects.create()

    def test_tags_create(self):
        data = {
            'url': 'https://rezka.ag/films/drama/176-poka-ya-zhiv-2012.html'
        }
        response = self.client.post(reverse('tags_create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('pk'), 3)

    def test_tags_create_fail(self):
        data = {
            'url': 'asd'
        }
        response = self.client.post(reverse('tags_create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_null_tags_counter_detail(self):
        response = self.client.get(reverse('tags_detail', kwargs={
            'pk': self.null_tags_counter.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_not_null_tags_counter_detail(self):
        response = self.client.get(reverse('tags_detail', kwargs={
            'pk': self.not_null_tags_counter.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), self.page_counts)

    def test_fail_tags_detail(self):
        response = self.client.get(reverse('tags_detail', kwargs={'pk': 50}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
