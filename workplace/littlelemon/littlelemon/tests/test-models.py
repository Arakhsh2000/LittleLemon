from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu  # Import your Menu model

class MenuModelTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_url = reverse('menu-list')

        # Correct field names to match  model
        Menu.objects.create(Title="Item3", Price=10, Inventory=20)

    def test_getall(self):
        response = self.client.get(self.menu_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Item3")
        # Add more assertions based on the expected behavior of your view
