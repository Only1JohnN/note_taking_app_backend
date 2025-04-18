# Mixins and GenericAPIView for Notes and Tags

from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .models import NotesModel
from .serializers import NotesSerializer, NotesDetailSerializer, TagSerializer
from taggit.models import Tag


class NotesListCreateAPIView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    GenericAPIView
    ):
    """Handles listing and creating notes."""
    queryset = NotesModel.objects.all()
    serializer_class = NotesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NotesRetrieveUpdateDestroyAPIView(
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    GenericAPIView
):
    """Handles retrieving, updating, and deleting a note."""
    queryset = NotesModel.objects.all()
    serializer_class = NotesDetailSerializer
    lookup_field = "id"  # Use `id` instead of `pk` for object lookup

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TagListCreateAPIView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    GenericAPIView
    ):
    
    """Handles listing and creating tags."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TagRetrieveUpdateDestroyAPIView(
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.DestroyModelMixin, 
    GenericAPIView
):
    """Handles retrieving, updating, and deleting a tag."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


