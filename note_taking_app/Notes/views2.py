from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from .models import NotesModel
from .serializers import NotesSerializer, NotesDetailSerializer, TagSerializer
from taggit.models import Tag


class NotesPagination(PageNumberPagination):
    page_size = 3  # Customize the number of items per page


class NotesListAPIView(ListCreateAPIView):
    queryset = NotesModel.objects.all()
    serializer_class = NotesSerializer
    pagination_class = NotesPagination


class NotesDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = NotesModel.objects.all()
    serializer_class = NotesDetailSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        try:
            note = self.get_object()
        except NotesModel.DoesNotExist:
            return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(note)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        try:
            note = self.get_object()
        except NotesModel.DoesNotExist:
            return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            note = self.get_object()
        except NotesModel.DoesNotExist:
            return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

        note.delete()
        return Response({"message": "Note deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer