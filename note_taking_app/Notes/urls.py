from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views2 import NotesListAPIView, NotesDetailAPIView, TagViewSet


router = DefaultRouter()
router.register(r'tags', TagViewSet)


urlpatterns = [
    # For views.py
    path('notes/', NotesListAPIView.as_view(), name='notes-list'),
    # path('notes/<int:note_id>/', NotesDetailAPIView.as_view(), name='note-detail'),
    # path('notes/update/<int:note_id>/', NotesDetailAPIView.as_view(), name='note-update'),
    # path('notes/delete/<int:note_id>/', NotesDetailAPIView.as_view(), name='note-delete'),
    path('', include(router.urls)),
    
    # For views2.py
    # path('notes/', NotesListAPIView.as_view(), name='notes-list'),
    path('notes/<int:pk>/', NotesDetailAPIView.as_view(), name='note-detail'),
    path('notes/update/<int:pk>/', NotesDetailAPIView.as_view(), name='note-update'),
    path('notes/delete/<int:pk>/', NotesDetailAPIView.as_view(), name='note-delete'),
    # path('', include(router.urls)),
]
