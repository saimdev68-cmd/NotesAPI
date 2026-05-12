from .models import Note
from .serializers import NoteSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.filters import SearchFilter , OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from accounts.pagination import PaginationNumber

# Create your views here.

class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PaginationNumber
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    ordering_fields = ["created_at"]
    search_fields = ["title"]
    filterset_fields = ["user"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Note.objects.select_related("user").all()
        return Note.objects.select_related("user").filter(user=user)
    
    @action(methods=["POST"], detail=True, permission_classes=[IsAuthenticated])
    def pin(self, request, pk):
        note = get_object_or_404(Note, pk=pk, user=request.user)
        if note.is_pinned:
            note.is_pinned = False
            note.save()
            return Response({"detail": "Note unpinned"})
        pinned_count = Note.objects.filter(user=request.user, is_pinned=True).count()
        if pinned_count >= 3:
            return Response({"detail": "You can only pin 3 notes"}, status=400)
        note.is_pinned = True
        note.save()
        return Response({"detail": "Note pinned"})