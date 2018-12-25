from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name_item', 'category', 'brand_item', 'type_item', 'note', 'cdUPC', 'is_active')
    search_fields = ('name_item',)
    # list_filter = ('modified', 'created')
    # date_hierarchy = 'modified'
    list_per_page = 18
    ordering = ['name_item']


admin.site.register(Item, ItemAdmin)
