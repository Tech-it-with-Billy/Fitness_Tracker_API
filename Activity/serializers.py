from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']