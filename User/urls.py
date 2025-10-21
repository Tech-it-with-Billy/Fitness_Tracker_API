from django.urls import path
from .views import UserProfileListCreateAPIView, UserProfileRetrieveUpdateDestroyAPIView, user_login, register, homepage, profile

urlpatterns = [
    path('', homepage, name=''),
    path('register', register, name= 'register'),
    path('login', user_login, name= 'login'),
    path('profile', profile, name= 'profile'),
    path('api/users/', UserProfileListCreateAPIView.as_view(), name='userprofile-list-create'),
    path('api/users/<int:pk>/', UserProfileRetrieveUpdateDestroyAPIView.as_view(), name='userprofile-detail'),

]