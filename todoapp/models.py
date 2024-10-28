from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=255)  
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # Default value for created_at

    def __str__(self):
        return self.title
