from django.db import models

# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=70)
    complete=models.BooleanField(blank=True, default=False, null=True)
    
    def __str__(self):
        return self.name
