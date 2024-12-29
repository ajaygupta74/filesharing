from rest_framework import serializers
from services.models import File


class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = (
            'title',
            'description',
            'user',
            'uploaded_at')
