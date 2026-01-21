from rest_framework import viewsets
from ..models.tag import Tag
from ..serializers.tag_serializers import TagSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer