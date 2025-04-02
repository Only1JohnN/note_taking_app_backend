from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotesListAPIView, NotesDetailAPIView, TagViewSet


router = DefaultRouter()
router.register(r'tags', TagViewSet)


urlpatterns = [
    path('notes/', NotesListAPIView.as_view(), name='notes-list'),
    path('notes/<int:note_id>/', NotesDetailAPIView.as_view(), name='note-detail'),
    path('notes/update/<int:note_id>/', NotesDetailAPIView.as_view(), name='note-update'),
    path('notes/delete/<int:note_id>/', NotesDetailAPIView.as_view(), name='note-delete'),
    path('', include(router.urls)),
]
