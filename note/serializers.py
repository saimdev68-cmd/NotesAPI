from .models import Note
from rest_framework import serializers
from accounts.serializers import UserSerializer

class NoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Note
        fields = ["id","user","title","content","created_at","is_pinned","pinned_time"]
        read_only_fields = ["created_at","is_pinned","pinned_time"]