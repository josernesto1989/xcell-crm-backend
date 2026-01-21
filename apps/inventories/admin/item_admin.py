from django.contrib import admin
from ..models.item import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    # What to show in the list view
    list_display = ('id', 'piece_type', 'description', 'quantity', 'sale_price_display')
    
    # Sidebar filters
    list_filter = ('piece_type', 'created_at')
    
    # Search functionality
    search_fields = ('description', 'piece_type__name')
    
    # Many-to-many UI improvement
    filter_horizontal = ('tags',)

    # Custom method to display price in a readable way
    def sale_price_display(self, obj):
        return f"${obj.sale_price_cents / 100:.2 f}"
    sale_price_display.short_description = 'Sale Price'