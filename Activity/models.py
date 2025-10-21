from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    ACTIVITY_CHOICE = [
        ('Running', 'Running'),
        ('Cycling', 'Cycling'),
        ('Swimming', 'Swimming'),
        ('Walking', 'Walking'),
        ('Gym', 'Gym'),
        ('Other', 'Other'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length= 50, choices=ACTIVITY_CHOICE)
    title = models.CharField(max_length=100)
    duration = models.DurationField(help_text='Activity duration')
    distance = models.FloatField(null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    def __str__(self):
        return f'{self.activity_type} - {self.title} ({self.user.username})'
    