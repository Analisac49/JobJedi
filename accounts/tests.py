from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AccountsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 302)  

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  

    def test_register_view(self):
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password1': 'newpass', 'password2': 'newpass'})
        self.assertEqual(response.status_code, 302)  
