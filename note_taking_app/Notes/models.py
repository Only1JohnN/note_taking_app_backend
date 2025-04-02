# models.py
from django.db import models
from taggit.managers import TaggableManager

class NotesModel(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    tags = TaggableManager()  # This is how we associate tags with notes

    def __str__(self):
        return self.title
