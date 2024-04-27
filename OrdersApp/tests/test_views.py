import json
from django.test import Client, TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from CustomersApp.models import Customer

from OrdersApp.models import Order

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.token = self.obtain_token()
    
    def obtain_token(self):
        # Create a user
        user = User.objects.create(username='admin')
        
        # Create a token for the user
        token = Token.objects.create(user=user)
        
        return token.key
        


    def test_all_orders_list_get(self):
        url = reverse('order_list')
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token}")
        self.assertEqual(response.status_code, 200)

    def test_single_order_list_get(self):
        # Create a user
        user = Customer.objects.create(name='test_user')
        # Create a test order associated with the user
        order = Order.objects.create(
            customer=user,
            item='Test item',
            amount='10.00',
        )

        url = reverse('order_detail', args=[order.pk])
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token}")

        self.assertEqual(response.status_code, 200)

    def test_single_order_add_post(self):
        # Create a user
        user = Customer.objects.create(name='test_user')

        data = {
            "item": "book",
            "amount": "12.00",
            "customer": user.id
        }
        url = reverse('order_list')

        response = self.client.post(url, data, HTTP_AUTHORIZATION=f"Token {self.token}")
        self.assertEqual(response.status_code, 201)
    
    def test_single_order_delete(self):
        # Create a user
        user = Customer.objects.create(name='test_user')
        # Create a test order associated with the user
        order = Order.objects.create(
            customer=user,
            item='Test item',
            amount='10.00',
        )

        # Get the URL for the order detail view
        url = reverse('order_detail', args=[order.pk])

        # Send a DELETE request to delete the order
        response = self.client.delete(url, HTTP_AUTHORIZATION=f"Token {self.token}")

        # Check if the response status code is 204 (No Content), indicating successful deletion
        self.assertEqual(response.status_code, 204)

        # Check if the order is deleted from the database
        self.assertFalse(Order.objects.filter(pk=order.pk).exists())