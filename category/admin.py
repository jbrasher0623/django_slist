from django.contrib import admin
from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_category', 'is_food', 'modified_by', 'created_by', 'is_active')
    search_fields = ('name_category',)
#     list_filter = ('modified', 'created')
#     date_hierarchy = 'modified'
    list_per_page = 18
    ordering = ['name_category']


admin.site.register(Category, CategoryAdmin)
