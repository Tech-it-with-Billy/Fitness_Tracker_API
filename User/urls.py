from django.urls import path, include
from .views import UserProfileListCreateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserProfileListCreateView, basename='userprofile')

urlpatterns = [
    path('api/', include(router.urls)), 
]