from django.contrib import admin
from ..models.tag import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'value')
    list_filter = ('key',)
    search_fields = ('key', 'value')