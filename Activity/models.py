from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Activity(models.Model):
    ACTIVITY_CHOICE = [
        ('Running', 'Running'),
        ('Cycling', 'Cycling'),
        ('Swimming', 'Swimming'),
        ('Walking', 'Walking'),
        ('Gym', 'Gym'),
        ('Other', 'Other'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities', null=True, blank=True)
    activity_type = models.CharField(max_length= 50, choices=ACTIVITY_CHOICE, null=True, blank=True)
    duration = models.DurationField(help_text='Activity duration')
    distance = models.FloatField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    calories_burned = models.FloatField(null=True, blank=True)
    date = models.DateField(default=timezone.localdate)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date', '-created_at']
    
    def __str__(self):
        return f'{self.activity_type} - {self.date}'
    