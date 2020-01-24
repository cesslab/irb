from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse


class SignUpTests(SimpleTestCase):

    def test_status_code(self):
        response = self.client.get('/accounts/signup')
        self.assertEquals(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse('signup'))

