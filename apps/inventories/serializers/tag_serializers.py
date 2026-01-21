from rest_framework import serializers
from ..models.tag import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'key', 'value']
        # 'id' is read_only by default in ModelSerializers