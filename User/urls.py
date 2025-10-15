from django.urls import path
from .views import UserProfileListCreateAPIView, UserProfileRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/users/', UserProfileListCreateAPIView.as_view(), name='userprofile-list-create'),
    path('api/users/<int:pk>/', UserProfileRetrieveUpdateDestroyAPIView.as_view(), name='userprofile-detail'),
]