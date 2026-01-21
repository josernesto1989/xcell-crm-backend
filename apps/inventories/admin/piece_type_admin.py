from django.contrib import admin
from ..models.piece_type import PieceType

@admin.register(PieceType)
class PieceTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)