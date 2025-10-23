from django.urls import path, include
from .views import register_user, login_user, logout_user, UserProfileViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet, basename='UserProfileViewSet')


urlpatterns = [
    path('register/', register_user, name = 'register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', logout_user, name='logout'),
    path('', include(router.urls)),
]