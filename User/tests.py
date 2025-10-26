from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status
from django.contrib.auth.models import User
from .views import register_user, login_user, UserProfileViewSet
from .models import UserProfile


class UserViewTests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='billy', password='12345', email='billy@test.com')
        self.profile = UserProfile.objects.create(
            user=self.user, gender='Male', height=175, weight=70, fitness_level='Intermediate'
        )

    def test_register_user(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@test.com',
            'password': 'newpassword123'
        }
        request = self.factory.post('api/user/register/', data, format='json')
        response = register_user(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('user', response.data)
        self.assertEqual(response.data['user']['username'], 'newuser')
        self.assertIn('tokens', response.data)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_user_success(self):
        data = {'username': 'billy', 'password': '12345'}
        request = self.factory.post('api/user/login/', data, format='json')
        response = login_user(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('tokens', response.data)
        self.assertIn('access', response.data['tokens'])

    def test_login_user_failure(self):
        data = {'username': 'billy', 'password': 'wrongpass'}
        request = self.factory.post('api/user/login/', data, format='json')
        response = login_user(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('error', response.data)

    def test_get_user_profile(self):
        view = UserProfileViewSet.as_view({'get': 'list'})
        request = self.factory.get('/api/user/profile/')
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        results = response.data.get('results', response.data)
        self.assertGreaterEqual(len(results), 1)
        self.assertEqual(results[0]['user'], self.user.id)