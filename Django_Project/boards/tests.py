from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from .views import home

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
#This is a very simple test case but extremely useful. We are testing the status code of the response. The status code 200 means success.

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)
