from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import NotesModel
from .serializers import NotesSerializer, NotesDetailSerializer, TagSerializer
from taggit.models import Tag


class NotesListAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = NotesSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def get(self, request, *args, **kwargs):
        notes = NotesModel.objects.all()
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NotesDetailAPIView(APIView):
    def get(self, request, note_id, *args, **kwargs):
        try:
            note = NotesModel.objects.get(id=note_id)
        except NotesModel.DoesNotExist:
            return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = NotesDetailSerializer(note)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, note_id, format=None):
        try:
            note = NotesModel.objects.get(id=note_id)
        except NotesModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = NotesDetailSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, note_id, format=None):
        try:
            note = NotesModel.objects.get(id=note_id)
        except NotesModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    

# class TagListAPIView(APIView):
#     """Handles listing and creating tags"""

#     def get(self, request):
#         tags = Tag.objects.all()
#         serializer = TagSerializer(tags, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = TagSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class TagDetailAPIView(APIView):
#     """Handles retrieving, updating, and deleting a tag"""

#     def get_object(self, tag_id):
#         try:
#             return Tag.objects.get(id=tag_id)
#         except Tag.DoesNotExist:
#             return None

#     def get(self, request, tag_id):
#         tag = self.get_object(tag_id)
#         if not tag:
#             return Response({"error": "Tag not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = TagSerializer(tag)
#         return Response(serializer.data)

#     def put(self, request, tag_id):
#         tag = self.get_object(tag_id)
#         if not tag:
#             return Response({"error": "Tag not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = TagSerializer(tag, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, tag_id):
#         tag = self.get_object(tag_id)
#         if not tag:
#             return Response({"error": "Tag not found"}, status=status.HTTP_404_NOT_FOUND)

#         tag.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)