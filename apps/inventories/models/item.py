from django.db import models
from .piece_type import PieceType
from .tag import Tag

class Item(models.Model):
    piece_type = models.ForeignKey(
        PieceType, 
        on_delete=models.PROTECT, 
        related_name='items'
    )
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='items', blank=True)
    
    # New fields for inventory management
    quantity = models.PositiveIntegerField(default=0) # Current stock
    min_quantity = models.PositiveIntegerField(default=0)
    max_quantity = models.PositiveIntegerField(default=0)
    
    # New fields for pricing (stored in cents)
    cost_price_cents = models.PositiveIntegerField(default=0)
    sale_price_cents = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.piece_type.name} - {self.description[:30]}"