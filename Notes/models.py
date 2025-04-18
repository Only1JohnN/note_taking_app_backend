from django.db import models
from taggit.managers import TaggableManager
from django.core.validators import MinLengthValidator
from django.utils import timezone

class NotesModel(models.Model):
    title = models.CharField(
        max_length=100, 
        blank=False, 
        null=False, 
        validators=[MinLengthValidator(5)]  # Minimum length of 5 characters
    )
    body = models.TextField(
        blank=False, 
        null=False, 
        validators=[MinLengthValidator(10)]  # Minimum length of 10 characters
    )
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
