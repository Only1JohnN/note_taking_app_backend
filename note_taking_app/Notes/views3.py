# Function-Based View

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from Notes.models import NotesModel
from Notes.serializers import NotesSerializer, NotesDetailSerializer, TagSerializer
from taggit.models import Tag


@api_view(["POST", "GET"])
def notes_list(request):
    if request.method == "POST":
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "GET":
        notes = NotesModel.objects.all()
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def notes_detail(request, note_id):
    try:
        note = NotesModel.objects.get(id=note_id)
    except NotesModel.DoesNotExist:
        return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = NotesDetailSerializer(note)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = NotesDetailSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# @api_view(["GET", "POST"])
# def tag_list_create(request):
#     """Handles listing and creating tags"""
#     if request.method == "GET":
#         tags = Tag.objects.all()
#         serializer = TagSerializer(tags, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = TagSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", "DELETE"])
# def tag_detail(request, tag_id):
#     """Handles retrieving, updating, and deleting a tag"""
#     try:
#         tag = Tag.objects.get(id=tag_id)
#     except Tag.DoesNotExist:
#         return Response({"error": "Tag not found"}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = TagSerializer(tag)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = TagSerializer(tag, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         tag.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)