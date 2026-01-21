from rest_framework import viewsets
from ..models.piece_type import PieceType
from ..serializers.piece_type_serializers import PieceTypeSerializer

class PieceTypeViewSet(viewsets.ModelViewSet):
    queryset = PieceType.objects.all()
    serializer_class = PieceTypeSerializer