from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views2 import NotesListAPIView, NotesDetailAPIView, TagViewSet


router = DefaultRouter()
# router.register(r'notes', NotesViewSet, basename='notes')
router.register(r'tags', TagViewSet)


urlpatterns = [
    # For views2.py - The paths for notes (CRUD operations)
    path('notes', NotesListAPIView.as_view(), name='home'),  # Default view to show the list of notes
    path('notes/<int:pk>/', NotesDetailAPIView.as_view(), name='note-detail'),  # Retrieve a specific note by pk
    path('notes/update/<int:pk>/', NotesDetailAPIView.as_view(), name='note-update'),  # Update a specific note by pk
    path('notes/delete/<int:pk>/', NotesDetailAPIView.as_view(), name='note-delete'),  # Delete a specific note by pk
    
    # Tags route handled by the router (uses TagViewSet)
    path('tags/', include(router.urls)),
    
    # For views.py
    # path('notes/', NotesListAPIView.as_view(), name='notes-list'),
    # path('notes/<int:note_id>/', NotesDetailAPIView.as_view(), name='note-detail'),
    # path('notes/update/<int:note_id>/', NotesDetailAPIView.as_view(), name='note-update'),
    # path('notes/delete/<int:note_id>/', NotesDetailAPIView.as_view(), name='note-delete'),
]
