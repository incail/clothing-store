from datetime import timedelta
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from .forms import UserLoginForm
from .models import EmailVerification, User


class RegistrationViewTestCase(TestCase):

    def setUp(self):
        self.data = {
            'first_name': 'ilya', 'last_name': 'veremeev',
            'username': 'incail', 'email': 'vel@gmail.com',
            'password1': '12345678pP', 'password2': '12345678pP'
        }
        self.path = reverse('users:registration')

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertEquals(response.context_data['title'], 'Store - Регистрация')
        self.assertTemplateUsed(response, 'users/register.html')

    def test_user_registration_post(self):
        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())

        response = self.client.post(self.path, self.data)

        self.assertEquals(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        email_verification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())
        self.assertEquals(
            email_verification.first().expiration.date(),
            (now() + timedelta(hours=48)).date()
        )

    def test_user_registration_post_error(self):
        User.objects.create(username=self.data['username'])

        response = self.client.post(self.path, self.data)

        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)


class UserLoginViewTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='Test',
            password='12345678pP',
            email='testuser@example.com',
            is_verified_email=True
        )

        self.path = reverse('users:login')

    def test_user_login_get(self):
        response = self.client.get(self.path)

        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertEquals(response.context_data['title'], 'Store - Вход')
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertIsInstance(response.context['form'], UserLoginForm)

    def test_user_login_post(self):
        data = {
            'username': 'Test',
            'password': '12345678pP'
        }
        response = self.client.post(self.path, data)

        self.assertRedirects(response, reverse('index'))

    def test_user_login_post_error(self):
        data = {
            'username': 'Test123',
            'password': '12345678pP'
        }
        response = self.client.post(self.path, data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertIn('form', response.context)
        self.assertTrue(response.context['form'].errors)
