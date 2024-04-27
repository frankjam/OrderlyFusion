from django.test import SimpleTestCase
from django.urls import reverse, resolve
from OrdersApp.views import OrderDetailAPIView, OrdersAPIView

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolve(self):
        url = reverse('order_list')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, OrdersAPIView)

    def test_details_url_is_resolve(self):
        url = reverse('order_detail',args=[1])
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, OrderDetailAPIView)