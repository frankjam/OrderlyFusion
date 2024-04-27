from django.test import SimpleTestCase
from django.urls import reverse, resolve
from CustomersApp.views import CustomerAPIView, CustomerDetailAPIView 

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolve(self):
        url = reverse('customer-list')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, CustomerAPIView)

    def test_details_url_is_resolve(self):
        url = reverse('customer-detail',args=[1])
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, CustomerDetailAPIView)