#ViewSets for handling CRUD operations for notes and tags

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import NotesModel
from .serializers import NotesSerializer, NotesDetailSerializer, TagSerializer
from taggit.models import Tag


class NotesViewSet(viewsets.ModelViewSet):
    """Handles CRUD operations for notes."""
    queryset = NotesModel.objects.all()

    def get_serializer_class(self):
        """Return different serializers based on action."""
        if self.action in ["retrieve", "update", "partial_update"]:
            return NotesDetailSerializer
        return NotesSerializer


class TagViewSet(viewsets.ModelViewSet):
    """Handles CRUD operations for tags."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
