from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth.models import User
from rest_framework import status
from .views import ActivityViewSet
from .models import Activity
from datetime import timedelta, date

class ActivityViewSetTests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='billy', password='12345')
        self.admin = User.objects.create_superuser(username='admin', password='admin123', email='admin@test.com')
        self.view = ActivityViewSet.as_view({
            'get': 'list',
            'post': 'create'
        })
        self.activity_data = {
            'activity_type': 'Running',
            'duration': timedelta(hours=1),
            'distance': 5.0,
            'calories_burned': 400,
            'date': date.today()
        }

    def test_create_activity(self):
        request = self.factory.post('/activities/', self.activity_data, format='json')
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Activity.objects.count(), 1)
        self.assertEqual(Activity.objects.get().user, self.user)

    def test_get_activities_user(self):
        Activity.objects.create(user=self.user, **self.activity_data)
        another_user = User.objects.create_user(username='other', password='pass123')
        Activity.objects.create(user=another_user, **self.activity_data)

        request = self.factory.get('/activities/')
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_activities_admin(self):
        Activity.objects.create(user=self.user, **self.activity_data)
        Activity.objects.create(user=self.admin, **self.activity_data)

        request = self.factory.get('/activities/')
        force_authenticate(request, user=self.admin)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_summary_endpoint(self):
        Activity.objects.create(user=self.user, **self.activity_data)
        summary_view = ActivityViewSet.as_view({'get': 'summary'})

        request = self.factory.get('/activities/summary/')
        force_authenticate(request, user=self.user)
        response = summary_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('total_distance', response.data)
        self.assertIn('total_calories', response.data)
        
        
        