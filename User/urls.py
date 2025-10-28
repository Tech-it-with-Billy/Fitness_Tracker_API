from django.urls import path, include
from .views import register_user, login_user, logout_user, UserProfileViewSet, my_profile
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet, basename='UserProfileViewSet')


urlpatterns = [
    path('register/', register_user, name = 'register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('account/', my_profile, name='current_user'),
    path('', include(router.urls)),
]