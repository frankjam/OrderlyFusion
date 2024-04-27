import json
from django.test import Client, TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from CustomersApp.models import Customer

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
        


    def test_all_customers_list_get(self):
        url = reverse('customer-list')
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token}")
        self.assertEqual(response.status_code, 200)

    def test_customer_get(self):
        # Create a user
        user = Customer.objects.create(name='test_user')
  
        url = reverse('customer-detail', args=[user.id])
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Token {self.token}")

        self.assertEqual(response.status_code, 200)

    def test_single_order_add_customer(self):
       
        data = {
            "name": "test user",
            "code": "12",
            "phone":'1234567890',
            "email":"tesst@test.com"
        }
        url = reverse('customer-list')

        response = self.client.post(url, data, HTTP_AUTHORIZATION=f"Token {self.token}")
        self.assertEqual(response.status_code, 201)
    
    def test_single_customer_delete(self):
        # Create a user
        user = Customer.objects.create(name='test_user')
 
        # Get the URL for the order detail view
        url = reverse('customer-detail', args=[user.id])

        # Send a DELETE request to delete the order
        response = self.client.delete(url, HTTP_AUTHORIZATION=f"Token {self.token}")

        # Check if the response status code is 204 (No Content), indicating successful deletion
        self.assertEqual(response.status_code, 204)

        # Check if the order is deleted from the database
        self.assertFalse(User.objects.filter(pk=user.id).exists())