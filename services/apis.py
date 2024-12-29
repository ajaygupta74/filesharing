from rest_framework import (mixins, viewsets)
from rest_framework.permissions import IsAuthenticated
from services.models import File
from services.serializers import FileListSerializer


class ProductCategoryViewSet(viewsets.GenericViewSet,
                             mixins.ListModelMixin):
    queryset = File.objects.filter(is_active=True).order_by("-uploaded_at")
    serializer_class = FileListSerializer
