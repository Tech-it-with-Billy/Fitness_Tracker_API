from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in minutes")
    calories_burned = models.IntegerField()

    def __str__(self):
        return self.name
    
    