from rest_framework import serializers
from ..models.piece_type import PieceType

class PieceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PieceType
        fields = ['id', 'name']