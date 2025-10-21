from django.shortcuts import render
from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer
from django.http import HttpResponse
class UserProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'pk'

def homepage(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def user_login(request):
    return render(request, 'userlogin.html')

def profile(request):
    return render(request, 'profile.html')