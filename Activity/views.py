from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from .models import Activity
from .serializers import ActivitySerializer
from .permissions import IsOwnerOrAdmin

class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Activity.objects.all()
        return Activity.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)