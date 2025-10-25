from django.shortcuts import render
from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Activity
from .serializers import ActivitySerializer
from .permissions import IsOwnerOrAdmin
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from datetime import datetime
from rest_framework.pagination import PageNumberPagination

class ActivityPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['activity_type', 'date']
    ordering_fields = ['date', 'duration', 'calories_burned', 'distance']
    search_fields = ['activity_type']
    pagination_class = ActivityPagination
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Activity.objects.all()
        return Activity.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=False, methods=['get'], url_path='summary')
    def summary(self, request):
        user = request.user
        queryset = self.get_queryset()
        
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        activity_type = request.query_params.get('activity_type')
        
        if start_date:
            try:
                startdate = datetime.strptime(start_date, "%Y-%m-%d").date()
                queryset = queryset.filter(date__gte=startdate)
            except ValueError:
                return Response({'error': 'start_date must be YYYY-MM-DD'}, status=status.HTTP_400_BAD_REQUEST)
        if end_date:
            try:
                enddate = datetime.strptime(end_date, "%Y-%m-%d").date()
                queryset = queryset.filter(date__lte=enddate)
            except ValueError:
                return Response({'error': 'end_date must be YYYY-MM-DD'}, status=status.HTTP_400_BAD_REQUEST)
        if activity_type:
            queryset= queryset.filter(activity_type=activity_type)
            
        totals = queryset.aggregate(
            total_distance=Sum('distance'),
            total_calories=Sum('calories_burned'),
        )
        
        total_duration_seconds = 0
        for act in queryset:
            if act.duration:
                total_duration_seconds += int(act.duration.total_seconds())
        
        data = {
            'total_distance': totals.get('total_distance') or 0,
            'total_calories': totals.get('total_calories') or 0,
            'total_duration_seconds': total_duration_seconds,
            'activities_count': queryset.count()
        }
        return Response(data)