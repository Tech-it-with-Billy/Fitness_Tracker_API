from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']
        
    
    def validate(self, attrs):
        if not attrs.get('activity_type'):
            raise serializers.ValidationError("Activity type is required")
        if not attrs.get('duration'):
            raise serializers.ValidationError("Duration is required")
        return attrs