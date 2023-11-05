from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.views import MenuItemView
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer



class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(Title="Item1", Price=10, Inventory=20)

    def test_getall(self):
        # Retrieve all Menu objects
        client = APIClient()
        url = reverse('menu-list')  
        response = client.get(url)

        # Assert the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the data
        expected_data = MenuSerializer(Menu.objects.all(), many=True).data

        # Assert that the serialized data equals the response data
        self.assertEqual(response.data, expected_data)