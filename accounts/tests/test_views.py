from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model

User = get_user_model()


class SignUpTests(TestCase):

    def test_status_code(self):
        response = self.client.get('/accounts/signup')
        self.assertEquals(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse('signup'))

    def test_create_user(self):
        data = {
            'email': 'foofy@gmail.com',
            'password1': 'foofyis1007b34f$',
            'password2': 'foofyis1007b34f$'
        }

        response = self.client.post('/accounts/signup', data)
        print(User.objects.first().email)
        self.assertEqual(User.objects.count(), 1)