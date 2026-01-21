from rest_framework import viewsets
from ..models.item import Item
from ..serializers.item_serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    # Optimization: select_related for ForeignKey, prefetch_related for ManyToMany
    queryset = Item.objects.select_related('piece_type').prefetch_related('tags').all()
    serializer_class = ItemSerializer