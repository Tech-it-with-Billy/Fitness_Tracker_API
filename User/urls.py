from django.urls import path, include
from .views import register_user, login_user, logout_user, UserProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet, basename='UserProfileViewSet')


urlpatterns = [
    path('register/', register_user, name = 'register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', include(router.urls)),
]