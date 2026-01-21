from rest_framework import serializers
from ..models.item import Item
from .piece_type_serializers import PieceTypeSerializer
from .tag_serializers import TagSerializer

class ItemSerializer(serializers.ModelSerializer):
    # Nested Serializers: This enables "Read" depth
    # We set read_only=True because creating nested data usually 
    # requires overriding the .create() method.
    piece_type_detail = PieceTypeSerializer(source='piece_type', read_only=True)
    tags_detail = TagSerializer(source='tags', many=True, read_only=True)
    
    # Custom field to display price as a decimal string
    sale_price_display = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = [
            'id', 
            'description', 
            'quantity', 
            'min_quantity', 
            'max_quantity',
            'cost_price_cents', 
            'sale_price_cents',
            'sale_price_display', # Virtual field
            'piece_type',         # Accepts ID on Write
            'piece_type_detail',  # Returns Object on Read
            'tags',               # Accepts list of IDs on Write
            'tags_detail',        # Returns list of Objects on Read
            'created_at', 
            'updated_at'
        ]
        # We make the raw IDs write_only to keep the Read response clean
        extra_kwargs = {
            'piece_type': {'write_only': True},
            'tags': {'write_only': True},
        }

    def get_sale_price_display(self, obj):
        return f"{obj.sale_price_cents / 100:.2f}"