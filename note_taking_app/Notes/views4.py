#GenericView for CRUD Operations (generics.{GenericAPIView} = GenericView)

from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import NotesModel
from .serializers import NotesSerializer, NotesDetailSerializer, TagSerializer
from taggit.models import Tag


class NotesListCreateAPIView(generics.ListCreateAPIView):
    """Handles listing and creating notes."""
    queryset = NotesModel.objects.all()
    serializer_class = NotesSerializer


class NotesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Handles retrieving, updating, and deleting a note."""
    queryset = NotesModel.objects.all()
    serializer_class = NotesDetailSerializer
    lookup_field = "pk"


class TagViewSet(viewsets.ModelViewSet):
    """Handles CRUD operations for tags."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# class TagListCreateAPIView(ListCreateAPIView):
#     """Handles listing and creating tags"""
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer


# class TagRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     """Handles retrieving, updating, and deleting a tag"""
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer

