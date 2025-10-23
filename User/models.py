from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    FITNESS_LEVEL_CHOICE = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, blank=True)
    height = models.FloatField(null=True, blank=True, help_text='Height(cm)')
    weight = models.FloatField(null=True, blank=True, help_text='Weight(kg)')
    fitness_level = models.CharField(max_length=15, choices=FITNESS_LEVEL_CHOICE, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    