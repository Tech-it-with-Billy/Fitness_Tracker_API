from django.contrib.auth import authenticate, login, logout
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import UserProfile
from .serializers import RegisterSerializer, UserProfileSerializer
from .permissions import IsOwnerOrAdmin


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Registration successful'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    
    if user:
        login(request, user)
        return Response({'message': 'Login Successful'}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials!'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    logout(request)
    return Response({'message': 'Logout Successful'}, status=status.HTTP_200_OK)

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return UserProfile.objects.all()
        return UserProfile.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)