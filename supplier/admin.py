from django.contrib import admin
from .models import Supplier


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name_supplier',)
    search_fields = ('name_supplier',)
    # list_filter = ('modified', 'created')
    # date_hierarchy = 'modified'
    list_per_page = 18
    ordering = ['name_supplier']


admin.site.register(Supplier, SupplierAdmin)
